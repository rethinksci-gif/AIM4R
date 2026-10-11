"""Original-page reading and language-neutral evidence extraction."""

import json
import logging
from datetime import datetime, timezone
from typing import Any, Optional

import httpx

from .client import AIClient
from .prompting.common import UNTRUSTED_INPUT_RULE
from .utils import parse_json_response
from ..extractors import ExtractorRegistry
from ..models import ContentItem, EvidenceClaim, EvidenceRecord
from ..processing.content import select_content, split_content
from ..processing.evidence import (
    ACCESS_FULL_TEXT,
    ACCESS_RANK,
    classify_access,
    fulltext_candidates,
    quote_in_source,
    ungrounded_numbers,
)
from ..processing.profiles import LoadedProfile

logger = logging.getLogger(__name__)

NOT_REPORTED = "not reported"
_TEXT_FIELDS = (
    "material_system",
    "data_scale",
    "batches_or_lots",
    "conditions",
    "baseline",
    "validation_method",
    "validation_setting",
    "independent_replication",
    "event_date",
    "reading_entry",
)
_VALIDATION_SETTINGS = {"simulation", "lab", "pilot", "production", "mixed", NOT_REPORTED}


async def deep_read(
    item: ContentItem,
    extractors: ExtractorRegistry,
    client: httpx.AsyncClient,
    extractor_name: str = "trafilatura",
) -> bool:
    """Try to read the original page; return True when content improved.

    The item keeps its feed text when the page cannot be fetched or yields
    less text. The attempt and its outcome are recorded in metadata so the
    access level shown to readers reflects what was actually read.
    """
    if item.metadata.get("access_level") == ACCESS_FULL_TEXT:
        item.metadata.setdefault("access_note", "full text available from the feed or source")
        return False
    extractor = extractors.get(extractor_name)
    if extractor is None:
        return False

    current = split_content(item.content).main
    current_level = item.metadata.get("access_level") or classify_access(item)
    comments = split_content(item.content).comments
    attempts = []
    for url in fulltext_candidates(str(item.url)):
        text = await extractor.extract(url, client)
        if not text or len(text.strip()) <= len(current):
            attempts.append(f"{url}: no longer text")
            continue
        previous = (item.content, item.metadata.get("content_source"))
        item.content = text.strip() + (
            f"\n\n--- Top Comments ---\n{comments}" if comments else ""
        )
        item.metadata["content_source"] = "extracted_page"
        level = classify_access(item)
        if ACCESS_RANK.get(level, 0) <= ACCESS_RANK.get(current_level, 0):
            # Longer but no better (e.g. a landing page around the same
            # abstract): keep the cleaner feed text.
            item.content, item.metadata["content_source"] = previous
            attempts.append(f"{url}: page adds no access beyond {current_level}")
            continue
        item.metadata["fulltext_url"] = url
        item.metadata["access_level"] = level
        item.metadata["access_note"] = (
            f"read original page {url}"
            if level == ACCESS_FULL_TEXT
            else f"original page gave {level} only: {url}"
        )
        return True

    item.metadata["access_note"] = (
        "original page not readable beyond the feed text (" + "; ".join(attempts) + ")"
    )
    return False


def evidence_system_prompt(profile: LoadedProfile) -> str:
    return f"""{profile.evidence_prompt}

- {UNTRUSTED_INPUT_RULE}
- Report only what the supplied content states. Missing information is `not reported`, never a guess."""


def evidence_user_prompt(item: ContentItem, profile: LoadedProfile) -> str:
    settings = profile.definition.evidence
    content = select_content(
        split_content(item.content).main,
        settings.max_chars if settings else 30000,
        profile.definition.content.sampling,
    )
    return f"""Title: {item.title}
URL: {item.url}
Access level: {item.metadata.get('access_level', 'unknown')}

# Supplied content

{content or 'No content available.'}"""


def build_evidence_record(
    parsed: dict[str, Any],
    item: ContentItem,
    *,
    fetched_at: Optional[datetime] = None,
) -> EvidenceRecord:
    """Normalize model output and attach code-owned fields and checks."""
    source_text = f"{item.title}\n{split_content(item.content).main}"
    record_fields: dict[str, Any] = {}
    for field in _TEXT_FIELDS:
        value = parsed.get(field)
        if isinstance(value, list):
            value = "; ".join(str(part) for part in value if part)
        value = str(value).strip() if value not in (None, "") else ""
        record_fields[field] = value or (NOT_REPORTED if field != "reading_entry" else "")
    if record_fields["event_date"] in ("", NOT_REPORTED):
        record_fields["event_date"] = "unknown"
    if record_fields["validation_setting"] not in _VALIDATION_SETTINGS:
        record_fields["validation_setting"] = NOT_REPORTED
    if record_fields["independent_replication"] != "reported":
        record_fields["independent_replication"] = NOT_REPORTED

    # Field values carrying numbers absent from the source are dropped:
    # missing values stay missing instead of being filled in.
    dropped_fields = []
    for field in _TEXT_FIELDS:
        if field in {"event_date"}:
            continue
        value = record_fields[field]
        if value not in (NOT_REPORTED, "") and ungrounded_numbers(value, source_text):
            record_fields[field] = NOT_REPORTED if field != "reading_entry" else ""
            dropped_fields.append(field)

    claims = []
    quotes_dropped = 0
    for raw in parsed.get("claims") or []:
        if not isinstance(raw, dict) or not str(raw.get("claim", "")).strip():
            continue
        claim = EvidenceClaim(
            claim=str(raw.get("claim", "")).strip(),
            quote=str(raw.get("quote", "")).strip(),
            location=str(raw.get("location", "")).strip() or "unknown",
        )
        claim.quote_found = quote_in_source(claim.quote, source_text)
        if not claim.quote_found:
            quotes_dropped += 1
            continue
        claims.append(claim)

    results = []
    results_dropped = 0
    for value in parsed.get("results") or []:
        text = str(value).strip()
        if not text:
            continue
        if ungrounded_numbers(text, source_text):
            results_dropped += 1
            continue
        results.append(text)

    limitations = [str(value).strip() for value in parsed.get("limitations") or [] if str(value).strip()]

    meta = item.metadata
    return EvidenceRecord(
        access_level=meta.get("access_level") or classify_access(item),
        access_note=meta.get("access_note", ""),
        source_kind=meta.get("source_kind")
        or ("code" if item.source_type.value == "github" else "unknown"),
        evidence_role=meta.get("role") or "unknown",
        peer_review=meta.get("peer_review") or "unknown",
        published_at=item.published_at.date().isoformat(),
        fetched_at=(fetched_at or item.fetched_at or datetime.now(timezone.utc)).date().isoformat(),
        claims=claims[:5],
        results=results,
        limitations=limitations,
        checks={
            "kind": "citation_consistency",
            "quotes_kept": len(claims[:5]),
            "quotes_dropped": quotes_dropped,
            "results_dropped_ungrounded_numbers": results_dropped,
            "fields_dropped_ungrounded_numbers": dropped_fields,
        },
        **record_fields,
    )


class EvidenceExtractor:
    """Extract one shared evidence record per item."""

    def __init__(self, ai_client: AIClient):
        self.client = ai_client

    async def extract(self, item: ContentItem, profile: LoadedProfile) -> EvidenceRecord:
        system = evidence_system_prompt(profile)
        user = evidence_user_prompt(item, profile)
        parsed = None
        for _ in range(2):
            response = await self.client.complete(system=system, user=user, temperature=0)
            parsed = parse_json_response(response)
            if isinstance(parsed, dict):
                break
            user += "\n\nYour previous response was not a JSON object. Return only the JSON object."
        if not isinstance(parsed, dict):
            raise ValueError("Evidence extraction did not return a JSON object")
        record = build_evidence_record(parsed, item)
        if item.processing:
            item.processing.evidence = record
        return record


def evidence_prompt_block(record: EvidenceRecord) -> str:
    """Render the shared evidence record for the writing prompt."""
    payload = record.model_dump(mode="json", exclude={"checks", "access_note"})
    payload["claims"] = [
        {"claim": claim["claim"], "quote": claim["quote"], "location": claim["location"]}
        for claim in payload["claims"]
    ]
    return json.dumps(payload, ensure_ascii=False, indent=2)
