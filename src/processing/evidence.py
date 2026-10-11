"""Deterministic evidence bookkeeping and consistency checks.

Nothing here judges whether a claim is true. These helpers record how much of
the original was actually read, check that quoted excerpts and numbers in the
generated text can be traced back to the source, and tidy citations. The
checks are citation/consistency checks, not fact verification.
"""

import html
import re
import unicodedata
from typing import Iterable, Optional
from urllib.parse import urlsplit, urlunsplit

from ..models import ContentItem

# Access levels, ordered from most to least complete.
ACCESS_FULL_TEXT = "full_text"
ACCESS_ABSTRACT = "abstract_or_summary"
ACCESS_SNIPPET = "snippet"
ACCESS_TITLE_ONLY = "title_only"

FULL_TEXT_MIN_CHARS = 3000
ABSTRACT_MIN_CHARS = 300
# Paper landing pages can exceed the length bar with abstract, metadata and
# reference lists, so papers also need visible body sections.
PAPER_SOURCE_KINDS = {"preprint", "journal"}
_PAPER_SECTIONS = re.compile(
    r"(?im)^\s*(?:(?:\d+(?:\.\d+)*|[IVX]+)\.?\s+)?"
    r"(introduction|methods?|materials and methods|experimental(?: section| details)?|"
    r"results(?: and discussion)?|discussion|conclusions?|method details)\s*$"
)
_NUMBERED_HEADING = re.compile(r"(?m)^\s*(?:\d+(?:\.\d+)*|[IVX]+(?:-[A-Z])?)\.?\s+[A-Z][^\n.]{2,70}$")


def has_paper_sections(text: str) -> bool:
    """True when text shows a paper body: named sections or numbered headings."""
    named = {match.group(1).lower() for match in _PAPER_SECTIONS.finditer(text)}
    return len(named) >= 2 or len(_NUMBERED_HEADING.findall(text)) >= 3


ACCESS_RANK = {ACCESS_TITLE_ONLY: 0, ACCESS_SNIPPET: 1, ACCESS_ABSTRACT: 2, ACCESS_FULL_TEXT: 3}


def classify_access(item: ContentItem) -> str:
    """Return the access level implied by how the item's content was obtained.

    Search-engine snippets never count as reading the original; only page
    extraction or a full feed body of substantial length is ``full_text``,
    and for papers the text must also show body sections.
    """
    from .content import split_content

    text = split_content(item.content).main
    length = len(text)
    origin = item.metadata.get("content_source")
    if origin in {"extracted_page", "feed_content"} and length >= FULL_TEXT_MIN_CHARS:
        if item.metadata.get("source_kind") not in PAPER_SOURCE_KINDS or has_paper_sections(text):
            return ACCESS_FULL_TEXT
    if length >= ABSTRACT_MIN_CHARS:
        return ACCESS_ABSTRACT
    if length > 0:
        return ACCESS_SNIPPET
    return ACCESS_TITLE_ONLY


_ARXIV_PATH = re.compile(r"^/(abs|pdf|html)/(?P<id>\d{4}\.\d{4,5})(v\d+)?(\.pdf)?/?$")


def arxiv_id(url: str) -> Optional[str]:
    parsed = urlsplit(url)
    if not (parsed.hostname or "").endswith("arxiv.org"):
        return None
    match = _ARXIV_PATH.match(parsed.path)
    return match.group("id") if match else None


def fulltext_candidates(url: str) -> list[str]:
    """Return URLs worth trying for the readable original, best first.

    arXiv abstract pages only hold the abstract (already in the feed), so
    only the HTML rendering of the paper is tried; it does not exist for
    every paper.
    """
    identifier = arxiv_id(url)
    if identifier:
        return [f"https://arxiv.org/html/{identifier}"]
    return [url]


def history_key(url: str) -> str:
    """Stable cross-run identity for a URL (versions and tracking removed)."""
    identifier = arxiv_id(url)
    if identifier:
        return f"arxiv:{identifier}"
    parsed = urlsplit(url.strip())
    query = "&".join(
        part
        for part in parsed.query.split("&")
        if part and not part.lower().startswith(("utm_", "dgcid=", "fbclid=", "gclid="))
    )
    path = parsed.path.rstrip("/") or "/"
    return urlunsplit(("", (parsed.hostname or "").lower(), path, query, ""))


def normalize_for_match(text: str) -> str:
    text = unicodedata.normalize("NFKC", html.unescape(text or ""))
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = re.sub(r"[‐-―]", "-", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def quote_in_source(quote: str, source_text: str) -> bool:
    """True when the quote appears verbatim (whitespace/quote-normalized)."""
    needle = normalize_for_match(quote).strip(" .\"'")
    if len(needle) < 12:
        return False
    return needle in normalize_for_match(source_text)


_NUMBER = re.compile(r"(?<![\w.])(\d+(?:[.,]\d+)*)(?![\w])")


def extract_numbers(text: str) -> set[str]:
    """Return significant numerals in text, normalized (commas removed).

    Single digits are ignored: they are mostly list ordinals or prose
    ("two-step", "3 sections") and would drown the signal.
    """
    found = set()
    for match in _NUMBER.finditer(unicodedata.normalize("NFKC", text or "")):
        value = match.group(1).replace(",", "")
        value = value.rstrip(".")
        if len(value.replace(".", "")) <= 1:
            continue
        found.add(value)
    return found


def ungrounded_numbers(generated: str, *grounding: str) -> list[str]:
    """Numbers in generated text that appear nowhere in the grounding texts."""
    allowed: set[str] = set()
    for text in grounding:
        allowed |= extract_numbers(text)
    return sorted(extract_numbers(generated) - allowed)


_LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z\-']*(?:\s+[A-Za-z][A-Za-z\-']*)*")


def longest_latin_run_words(text: str) -> int:
    """Words in the longest run of Latin-script words (for zh purity checks)."""
    cleaned = re.sub(r"https?://\S+", " ", text or "")
    return max((len(run.split()) for run in _LATIN_RUN.findall(cleaned)), default=0)


def dedupe_sentences(blocks: Iterable[str]) -> list[str]:
    """Drop sentences that already appeared in an earlier block."""
    seen: set[str] = set()
    result = []
    for block in blocks:
        kept = []
        # Split after CJK terminators, or after .!? only when whitespace
        # follows, so decimals such as "1.81" are never broken apart.
        for sentence in re.split(r"(?<=[。！？])\s*|(?<=[.!?])\s+", block):
            key = normalize_for_match(sentence)
            if not key:
                continue
            if len(key) >= 8 and key in seen:
                continue
            seen.add(key)
            kept.append(sentence.strip())
        result.append(_join_sentences(kept))
    return result


_CJK_CHAR = re.compile(r"[　-〿一-鿿＀-￯]")


def _join_sentences(sentences: list[str]) -> str:
    text = ""
    for sentence in sentences:
        if text and not (_CJK_CHAR.match(text[-1]) or _CJK_CHAR.match(sentence[0])):
            text += " "
        text += sentence
    return text


_SPACED_PUNCT = re.compile(r"\s+([’'`,.:;!?)\]])|([(\[‘’'])\s+")


def clean_citation_title(title: str, url: str) -> str:
    """Tidy scraped page titles; fall back to the host name when unusable."""
    text = html.unescape(title or "")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([’'])\s+", r"\1", text)
    text = _SPACED_PUNCT.sub(lambda m: m.group(1) or m.group(2), text)
    text = re.sub(r"\s*(\.\.\.|…)$", "", text).strip(" -|·")
    if len(text) < 4:
        return (urlsplit(url).hostname or url).removeprefix("www.")
    return text


def dedupe_sources(sources: list, primary_url: str) -> list:
    """Remove sources without a URL, duplicates and the item's own URL."""
    seen = {history_key(primary_url)}
    result = []
    for source in sources:
        url = (getattr(source, "url", "") or "").strip()
        if not url.lower().startswith(("http://", "https://")):
            continue
        key = history_key(url)
        if key in seen:
            continue
        seen.add(key)
        source.title = clean_citation_title(source.title, url)
        result.append(source)
    return result
