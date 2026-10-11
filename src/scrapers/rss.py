"""RSS feed scraper implementation."""

import asyncio
import calendar
import hashlib
import html
import logging
import os
import re
import time
from datetime import datetime, timedelta, timezone
from typing import List, Optional, Tuple
from email.utils import parsedate_to_datetime
import httpx
import feedparser
from bs4 import BeautifulSoup

from .base import BaseScraper
from ..extractors import ExtractorRegistry
from ..models import ContentItem, SourceType, RSSSourceConfig

logger = logging.getLogger(__name__)

# Minimum seconds between consecutive requests to hosts that ask for it
# (arXiv API terms request roughly three seconds between calls).
_POLITE_HOST_DELAY = {"export.arxiv.org": 3.0}


class RSSScraper(BaseScraper):
    """Scraper for RSS/Atom feeds."""

    def __init__(
        self,
        sources: List[RSSSourceConfig],
        http_client: httpx.AsyncClient,
        extractors: Optional[ExtractorRegistry] = None,
    ):
        """Initialize RSS scraper.

        Args:
            sources: List of RSS feed configurations
            http_client: Shared async HTTP client
            extractors: Optional registry of content extractors for full article fetching
        """
        super().__init__({"sources": sources}, http_client)
        self._extractors = extractors
        # Per-feed failures from the last fetch, as (feed name, error) pairs.
        # A failing feed must not be reported as an empty one.
        self.source_failures: List[Tuple[str, str]] = []
        self.attempted_feeds = 0

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch RSS feed items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        items = []
        sources = self.config["sources"]
        self.source_failures = []
        self.attempted_feeds = 0
        last_host_request: dict[str, float] = {}

        for source in sources:
            if not source.enabled:
                continue
            self.attempted_feeds += 1
            host = source.url.host or ""
            delay = _POLITE_HOST_DELAY.get(host)
            if delay and host in last_host_request:
                wait = delay - (time.monotonic() - last_host_request[host])
                if wait > 0:
                    await asyncio.sleep(wait)
            last_host_request[host] = time.monotonic()

            feed_since = since
            if source.lookback_hours:
                feed_since = min(
                    since,
                    datetime.now(timezone.utc) - timedelta(hours=source.lookback_hours),
                )
            feed_items = await self._fetch_feed(source, feed_since)
            items.extend(feed_items)

        return items

    async def _fetch_feed(
        self, source: RSSSourceConfig, since: datetime
    ) -> List[ContentItem]:
        """Fetch items from a single RSS feed.

        Args:
            source: RSS feed configuration
            since: Only fetch items after this time

        Returns:
            List[ContentItem]: Feed content items
        """
        items = []

        try:
            # Expand environment variables in URL (e.g. ${LWN_TOKEN})
            feed_url = re.sub(
                r"\$\{(\w+)\}",
                lambda m: os.environ.get(m.group(1), m.group(0)).strip(),
                str(source.url),
            )

            # Fetch feed content
            response = await self.client.get(feed_url, follow_redirects=True)
            response.raise_for_status()

            # Parse feed
            feed = feedparser.parse(response.text)
            if not feed.entries and feed.get("bozo"):
                raise ValueError(
                    f"feed did not parse: {feed.get('bozo_exception') or 'no entries'}"
                )

            for entry in feed.entries:
                # Parse published date
                published_at = self._parse_date(entry)
                if not published_at or published_at < since:
                    continue

                # Extract content: prefer the fullest feed body as plain text.
                content, content_source = self._select_feed_content(entry)
                title = _clean_text(entry.get("title", "Untitled"))
                if not self._matches_keywords(source, f"{title}\n{content}"):
                    continue

                # Generate unique ID from feed URL and entry ID
                feed_id = str(source.url).split("//")[1].replace("/", "_")
                entry_id = entry.get("id", entry.get("link", ""))
                entry_hash = hashlib.sha256(str(entry_id).encode("utf-8")).hexdigest()[
                    :16
                ]

                if source.content_extractor and self._extractors:
                    extractor = self._extractors.get(source.content_extractor)
                    if extractor:
                        url = entry.get("link", "")
                        if url:
                            full = await extractor.extract(url, self.client)
                            # Keep the feed body when the page extraction is
                            # shorter (paywall stubs, cookie walls, etc.).
                            if full and len(full.strip()) > len(content):
                                content = full.strip()
                                content_source = "extracted_page"

                metadata = {
                    "feed_name": source.name,
                    "category": source.category,
                    "tags": [tag.term for tag in entry.get("tags", [])],
                    "content_source": content_source,
                }
                for key in ("role", "source_kind", "peer_review"):
                    value = getattr(source, key)
                    if value:
                        metadata[key] = value
                if entry.get("arxiv_announce_type"):
                    metadata["announce_type"] = entry.get("arxiv_announce_type")

                item = ContentItem(
                    id=self._generate_id("rss", feed_id, entry_hash),
                    source_type=SourceType.RSS,
                    title=title,
                    url=entry.get("link", str(source.url)),
                    content=content,
                    author=entry.get("author", source.name),
                    published_at=published_at,
                    profile=source.profile,
                    metadata=metadata,
                )
                items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching RSS feed %s: %s", source.name, e)
            self.source_failures.append((source.name, f"{type(e).__name__}: {e}"))
        except Exception as e:
            logger.warning("Error parsing RSS feed %s: %s", source.name, e)
            self.source_failures.append((source.name, f"{type(e).__name__}: {e}"))

        return items

    def _parse_date(self, entry: dict) -> datetime:
        """Parse publication date from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            datetime: Parsed publication date or None
        """
        # Try different date fields
        for field in ["published", "updated", "created"]:
            if field in entry:
                try:
                    # Try parsing structured time first
                    if f"{field}_parsed" in entry and entry[f"{field}_parsed"]:
                        return datetime.fromtimestamp(
                            calendar.timegm(entry[f"{field}_parsed"]), tz=timezone.utc
                        )
                    # Fallback to string parsing
                    date_str = entry[field]
                    return parsedate_to_datetime(date_str)
                except Exception:
                    continue

        return None

    @staticmethod
    def _select_feed_content(entry: dict) -> Tuple[str, str]:
        """Return the fullest feed body as plain text and where it came from.

        ``content`` (e.g. ``content:encoded``) usually carries the full post
        while ``summary`` is a teaser, so the longer of the two wins. Returns
        ``("", "none")`` when the entry has no body.
        """
        full = ""
        for part in entry.get("content") or []:
            value = _html_to_text(part.get("value", ""))
            if len(value) > len(full):
                full = value
        summary = _html_to_text(entry.get("summary") or entry.get("description") or "")
        if full and len(full) >= len(summary):
            return full, "feed_content"
        if summary:
            return summary, "feed_summary"
        return "", "none"

    @staticmethod
    def _matches_keywords(source: RSSSourceConfig, text: str) -> bool:
        haystack = text.lower()
        if any(word.lower() in haystack for word in source.exclude_keywords):
            return False
        return all(
            any(word.lower() in haystack for word in group)
            for group in source.keyword_groups
            if group
        )


def _clean_text(value: str) -> str:
    """Decode HTML entities (including double-encoded ones) and collapse spaces."""
    text = str(value)
    for _ in range(2):
        decoded = html.unescape(text)
        if decoded == text:
            break
        text = decoded
    return re.sub(r"\s+", " ", text).strip()


def _html_to_text(value: str) -> str:
    """Convert a feed HTML fragment to readable plain text."""
    if not value:
        return ""
    if "<" not in value:
        return _clean_text(value)
    soup = BeautifulSoup(value, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    blocks = [_clean_text(chunk) for chunk in soup.get_text("\n").split("\n")]
    return "\n".join(block for block in blocks if block)
