"""Build an editorial-preview edition from a hand-written spec.

The spec holds editor-written analysis, evidence and bilingual text for real
items. This script pushes it through the production code paths: it re-reads
each original (when --fetch is given), recomputes the access level, rebuilds
the evidence record with the same quote and number checks, runs the writing
quality checks on both languages, and renders with the production renderer.
Any failed check stops the build.

Outputs are marked ``preview: true`` and written to docs/_previews/, which
Jekyll excludes, so they are never published by the normal workflow.

Usage:
    uv run python scripts/build_preview_edition.py \
        --spec docs/_previews/source/2026-10-11-preview.json --out docs/_previews --fetch
"""

import argparse
import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.ai.enricher import artifact_quality_problems  # noqa: E402
from src.ai.evidence import build_evidence_record, deep_read  # noqa: E402
from src.ai.research_renderer import EditionStats, ResearchEditionRenderer  # noqa: E402
from src.extractors import ExtractorRegistry  # noqa: E402
from src.models import (  # noqa: E402
    ClassificationResult,
    ContentAnalysis,
    ContentArtifact,
    ContentBlock,
    ContentItem,
    ProcessingResult,
    SourceType,
)
from src.processing import ProfileRegistry  # noqa: E402
from src.processing.evidence import classify_access  # noqa: E402
from src.processing.rubric import apply_rubric  # noqa: E402

BLOCKS = ("why_read", "advance", "evidence", "significance", "boundaries", "next_step")


async def build_item(spec: dict, profile, client, registry, fetch: bool, fetched_on: datetime) -> ContentItem:
    item = ContentItem(
        id=f"preview:{spec['url']}",
        source_type=SourceType.RSS,
        title=spec["title"],
        url=spec["url"],
        content=spec.get("feed_text", ""),
        published_at=datetime.fromisoformat(spec["published_at"]).replace(tzinfo=timezone.utc),
        fetched_at=fetched_on,
        profile=profile.id,
        metadata={
            "feed_name": spec["feed_name"],
            "source_kind": spec["source_kind"],
            "role": spec["role"],
            "peer_review": spec["peer_review"],
            "content_source": "feed_summary" if spec.get("feed_text") else "none",
        },
    )
    item.metadata["access_level"] = classify_access(item)
    if fetch:
        await deep_read(item, registry, client)
    rubric = profile.definition.rubric
    raw = spec["analysis"]
    analysis = ContentAnalysis(
        reason="editor preview",
        summary=spec["title"],
        content_type=raw["content_type"],
        topic=raw["topic"],
        gates={gate: {"passed": passed, "reason": "editor judgment"} for gate, passed in raw["gates"].items()},
        dimensions={dim: {"score": score, "reason": reason} for dim, (score, reason) in raw["dimensions"].items()},
    )
    analysis = apply_rubric(analysis, rubric, topic_ids={t.id for t in profile.definition.topics})
    item.processing = ProcessingResult(
        classification=ClassificationResult(profile=profile.id, method="source_override"),
        analysis=analysis,
    )
    record = build_evidence_record(spec["evidence"], item, fetched_at=fetched_on)
    item.processing.evidence = record
    problems = []
    if fetch:
        dropped = record.checks.get("quotes_dropped") or 0
        if dropped:
            problems.append(f"{dropped} quote(s) not found in the text that was read")
        if record.checks.get("results_dropped_ungrounded_numbers"):
            problems.append("a result contains numbers not found in the text that was read")
        if record.checks.get("fields_dropped_ungrounded_numbers"):
            problems.append(f"fields with ungrounded numbers: {record.checks['fields_dropped_ungrounded_numbers']}")
    for language, text in spec["artifacts"].items():
        blocks = [
            ContentBlock(id=block_id, title=block_id, content=text[block_id], primary=block_id == "why_read")
            for block_id in BLOCKS
            if text.get(block_id)
        ]
        problems += [f"{language}: {p}" for p in artifact_quality_problems(text["title"], blocks, item, language)]
        item.processing.artifacts[language] = ContentArtifact(language=language, title=text["title"], blocks=blocks)
    if problems:
        raise SystemExit(f"Checks failed for {spec['title'][:60]}:\n  - " + "\n  - ".join(problems))
    print(
        f"  ok  [{analysis.track:7}] score={analysis.score} access={record.access_level} "
        f"quotes={record.checks['quotes_kept']} :: {spec['title'][:70]}"
    )
    return item


async def main_async(args) -> None:
    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    profiles = ProfileRegistry.load(ROOT / "profiles", "material-intel")
    profile = profiles.get("material-intel")
    fetched_on = datetime.fromisoformat(spec["date"]).replace(tzinfo=timezone.utc)
    registry = ExtractorRegistry({})
    async with httpx.AsyncClient(timeout=60.0) as client:
        items = [
            await build_item(entry, profile, client, registry, args.fetch, fetched_on)
            for entry in spec["items"]
        ]
    items.sort(key=lambda item: (item.processing.analysis.track == "explore", -item.processing.analysis.score))
    stats = EditionStats(**spec["stats"])
    renderer = ResearchEditionRenderer(profile.definition.topics)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for language in ("zh", "en"):
        edition = renderer.render(items, spec["date"], language, stats)
        edition.front_matter["preview"] = True
        edition.front_matter["preview_note"] = spec["preview_note"][language]
        edition.front_matter["issue_status"] = "editorial_preview"
        edition.front_matter["description"] = spec["preview_note"][language]
        body = edition.body.replace(
            edition.body.split("\n", 1)[0],
            '<p class="issue-lede">'
            + ("编辑预览：3 条真实来源，由编辑依据实际读到的原文撰写。" if language == "zh"
               else "Editorial preview: three real sources, written by the editor from the originals actually read.")
            + "</p>",
            1,
        )
        edition.body = body
        target = out / f"{spec['date']}-summary-{language}.md"
        target.write_text(edition.post_text(), encoding="utf-8")
        print(f"wrote {target}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--spec", required=True)
    parser.add_argument("--out", default="docs/_previews")
    parser.add_argument("--fetch", action="store_true", help="re-read originals and verify quotes/numbers against them")
    asyncio.run(main_async(parser.parse_args()))


if __name__ == "__main__":
    main()
