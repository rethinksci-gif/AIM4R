"""Verify configured RSS/Atom sources against the live network.

Runs the production RSS scraper feed by feed (no AI calls) and reports, for
each source: HTTP/parse outcome, entries in the lookback window, how many
passed the keyword filter, body length and origin, and sample titles. With
``--probe-pages`` it also tries the page extractor on the first kept item to
show whether the original is readable.

Usage:
    uv run python scripts/check_sources.py --config data/config.material-intel.json
    uv run python scripts/check_sources.py --config ... --hours 168 --probe-pages --json out.json
"""

import argparse
import asyncio
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.ai.evidence import deep_read  # noqa: E402
from src.extractors import ExtractorRegistry  # noqa: E402
from src.processing.evidence import classify_access  # noqa: E402
from src.scrapers.rss import RSSScraper  # noqa: E402
from src.storage.manager import StorageManager  # noqa: E402


async def check(config_path: str, hours: int, probe_pages: bool) -> list[dict]:
    config = StorageManager(config_path=config_path).load_config()
    since = datetime.now(timezone.utc) - timedelta(hours=hours)
    registry = ExtractorRegistry(config.extractors)
    report = []
    async with httpx.AsyncClient(
        timeout=40.0, headers={"User-Agent": "AIM4R-source-check/1.0"}
    ) as client:
        for source in config.sources.rss:
            if not source.enabled:
                continue
            row: dict = {"name": source.name, "url": str(source.url), "role": source.role,
                         "source_kind": source.source_kind}
            # Raw parse without filters, to separate "feed broken" from "filtered out".
            try:
                response = await client.get(str(source.url), follow_redirects=True)
                row["http_status"] = response.status_code
                parsed = feedparser.parse(response.text)
                row["entries_total"] = len(parsed.entries)
                row["entries_dated"] = sum(
                    1 for e in parsed.entries if e.get("published_parsed") or e.get("updated_parsed")
                )
            except Exception as exc:  # noqa: BLE001 - report every failure
                row["http_status"] = None
                row["error"] = f"{type(exc).__name__}: {exc}"
            window = source.model_copy(update={"keyword_groups": [], "exclude_keywords": [],
                                               "content_extractor": None})
            scraper = RSSScraper([window], client)
            unfiltered = await scraper.fetch(since)
            scraper = RSSScraper([source.model_copy(update={"content_extractor": None})], client)
            kept = await scraper.fetch(since)
            if scraper.source_failures:
                row["error"] = scraper.source_failures[0][1]
            row["in_window"] = len(unfiltered)
            row["kept_after_keywords"] = len(kept)
            row["window_hours"] = max(hours, source.lookback_hours or 0)
            if kept:
                row["newest"] = max(item.published_at for item in kept).date().isoformat()
                row["median_body_chars"] = sorted(len(item.content or "") for item in kept)[len(kept) // 2]
                row["body_origin"] = sorted({item.metadata.get("content_source") for item in kept})
                row["samples"] = [item.title[:110] for item in kept[:5]]
                if probe_pages:
                    item = kept[0]
                    item.metadata["access_level"] = classify_access(item)
                    before = item.metadata["access_level"]
                    improved = await deep_read(item, registry, client)
                    row["page_probe"] = {
                        "item": item.title[:80],
                        "access_before": before,
                        "access_after": item.metadata.get("access_level"),
                        "improved": improved,
                        "note": item.metadata.get("access_note", "")[:200],
                    }
            report.append(row)
            print(_line(row), flush=True)
    return report


def _line(row: dict) -> str:
    status = "FAIL" if row.get("error") else ("ok" if row.get("kept_after_keywords") else "quiet")
    text = (
        f"[{status:5}] {row['name']}: http={row.get('http_status')} entries={row.get('entries_total')} "
        f"dated={row.get('entries_dated')} in_window={row.get('in_window')} kept={row.get('kept_after_keywords')} "
        f"median_body={row.get('median_body_chars')} origin={row.get('body_origin')}"
    )
    if row.get("error"):
        text += f"\n        error: {row['error'][:160]}"
    for sample in row.get("samples", []):
        text += f"\n        - {sample}"
    if row.get("page_probe"):
        probe = row["page_probe"]
        text += f"\n        page probe: {probe['access_before']} -> {probe['access_after']} ({probe['note'][:100]})"
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config", default="data/config.material-intel.json")
    parser.add_argument("--hours", type=int, default=72)
    parser.add_argument("--probe-pages", action="store_true")
    parser.add_argument("--json", help="write the report as JSON to this path")
    args = parser.parse_args()
    report = asyncio.run(check(args.config, args.hours, args.probe_pages))
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
