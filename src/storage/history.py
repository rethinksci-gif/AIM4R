"""Cross-run history: seen items, published issues and run status.

The ledger lets a daily run use an overlapping lookback window without
re-surfacing items, keeps "nothing qualified" distinct from "sources failed",
and makes reruns predictable:

- Items are recorded only when a run finishes, so a crashed run leaves no
  trace and a rerun processes the same items again.
- Items that were screened or published are skipped in later runs.
- Items whose analysis or writing failed are not recorded and are retried
  while they stay inside the lookback window.
- A date that already has a published issue is not overwritten by a rerun.
"""

import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

from .._file_utils import _atomic_write_text
from ..models import ContentItem
from ..processing.evidence import history_key

RUN_LOG_LIMIT = 60

# Run statuses shown to readers.
PUBLISHED = "published"
PUBLISHED_DEGRADED = "published_degraded"
NO_QUALIFIED = "no_qualified"
NO_NEW_ITEMS = "no_new_items"
SOURCE_FAILURE = "source_failure"
PROCESSING_FAILURE = "processing_failure"
ALREADY_PUBLISHED = "already_published"


@dataclass
class RunRecord:
    date: str
    status: str
    fetched: int = 0
    new: int = 0
    screened: int = 0
    selected: int = 0
    failed_sources: list[str] = field(default_factory=list)
    note: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "date": self.date,
            "run_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "status": self.status,
            "fetched": self.fetched,
            "new": self.new,
            "screened": self.screened,
            "selected": self.selected,
            "failed_sources": self.failed_sources,
            "note": self.note,
        }


class RunHistory:
    """JSON-file ledger shared across runs."""

    def __init__(self, path: Path, retention_days: int = 120):
        self.path = Path(path)
        self.retention_days = retention_days
        self.data: dict[str, Any] = {"version": 1, "items": {}, "issues": {}, "runs": []}
        if self.path.exists():
            try:
                loaded = json.loads(self.path.read_text(encoding="utf-8") or "{}")
            except json.JSONDecodeError as exc:
                raise ValueError(f"History file is not valid JSON: {self.path}") from exc
            if isinstance(loaded, dict):
                self.data.update({k: v for k, v in loaded.items() if k in self.data})

    @staticmethod
    def key(item: ContentItem) -> str:
        return history_key(str(item.url))

    def seen(self, item: ContentItem) -> Optional[dict[str, Any]]:
        return self.data["items"].get(self.key(item))

    def split_unseen(
        self, items: Iterable[ContentItem]
    ) -> tuple[list[ContentItem], list[ContentItem]]:
        """Return (new items, items already handled in an earlier run)."""
        new, old = [], []
        batch_keys: set[str] = set()
        for item in items:
            key = self.key(item)
            if key in self.data["items"] or key in batch_keys:
                old.append(item)
            else:
                batch_keys.add(key)
                new.append(item)
        return new, old

    def issue(self, date: str) -> Optional[dict[str, Any]]:
        return self.data["issues"].get(date)

    def record_items(
        self,
        items: Iterable[ContentItem],
        status: str,
        date: str,
    ) -> None:
        for item in items:
            key = self.key(item)
            entry = self.data["items"].get(key, {})
            analysis = item.processing.analysis if item.processing else None
            entry.update(
                {
                    "title": item.title[:200],
                    "url": str(item.url),
                    "published_at": item.published_at.date().isoformat(),
                    "first_seen": entry.get("first_seen", date),
                    "last_seen": date,
                    "status": status if entry.get("status") != PUBLISHED else PUBLISHED,
                }
            )
            if analysis is not None:
                entry["score"] = analysis.score
                if analysis.track:
                    entry["track"] = analysis.track
                if analysis.rejected_by:
                    entry["rejected_by"] = analysis.rejected_by
            if status == PUBLISHED:
                entry["issue"] = date
            self.data["items"][key] = entry

    def record_issue(self, date: str, items: list[ContentItem], languages: list[str]) -> None:
        self.data["issues"][date] = {
            "status": PUBLISHED,
            "items": [self.key(item) for item in items],
            "languages": languages,
        }

    def record_run(self, record: RunRecord) -> None:
        runs = self.data["runs"]
        runs.insert(0, record.to_dict())
        del runs[RUN_LOG_LIMIT:]

    def prune(self, today: Optional[datetime] = None) -> None:
        today = today or datetime.now(timezone.utc)
        cutoff = (today - timedelta(days=self.retention_days)).date().isoformat()
        self.data["items"] = {
            key: entry
            for key, entry in self.data["items"].items()
            if entry.get("status") == PUBLISHED or entry.get("last_seen", "") >= cutoff
        }

    def save(self) -> None:
        self.prune()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        _atomic_write_text(
            self.path,
            json.dumps(self.data, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
        )
