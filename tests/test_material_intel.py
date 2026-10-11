"""Offline tests for the material-intel research edition.

All AI calls go to a scripted fake; all inputs are mock fixtures. These tests
check the engine's deterministic behavior (gates, floors, access levels,
grounding checks, history, statuses, rendering). They cannot show that a
real model judges items well; that needs a reviewed live run.
"""

from __future__ import annotations

import asyncio
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
from unittest.mock import AsyncMock, MagicMock

import pytest
from rich.console import Console

from src.ai.analyzer import ContentAnalyzer
from src.ai.enricher import ContentEnricher, artifact_quality_problems
from src.ai.evidence import EvidenceExtractor, build_evidence_record, deep_read
from src.ai.prompting.analysis import analysis_system_prompt
from src.ai.research_renderer import EditionStats, ResearchEditionRenderer
from src.ai.summarizer import _escape_markdown
from src.models import (
    AIConfig,
    ArtifactSource,
    ClassificationResult,
    CollectionConfig,
    Config,
    ContentAnalysis,
    ContentItem,
    DigestConfig,
    ProcessingConfig,
    ProcessingResult,
    ProfileSettingsConfig,
    RSSSourceConfig,
    SourcesConfig,
    SourceType,
)
from src.orchestrator import FetchReport, HorizonOrchestrator, SourceFetchOutcome
from src.processing import ProfileRegistry
from src.processing.evidence import (
    classify_access,
    dedupe_sentences,
    dedupe_sources,
    history_key,
)
from src.scrapers.rss import RSSScraper
from src.storage.history import RunHistory
from src.storage.manager import StorageManager

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "material_intel"
PROFILES = ProfileRegistry.load(ROOT / "profiles", "material-intel")
PROFILE = PROFILES.get("material-intel")
NOW = datetime(2026, 10, 11, 6, 0, tzinfo=timezone.utc)

MOCK_BODY = (
    "MOCK ARTICLE. We study recycled polypropylene (rPP) blends from three suppliers.\n"
    "Methods\nAn active learning loop with a Gaussian process surrogate proposed 48 "
    "formulations across 6 resin lots.\nResults\nThe loop reached the target melt flow "
    "index in 19 experiments versus 41 for a full factorial baseline.\n"
    "Don't over-read this: validation used one extruder."
)


# ---------------------------------------------------------------- helpers


class ScriptedAI:
    """Fake AI client that answers via a router and records every call."""

    def __init__(self, router: Callable[[str, str], str]):
        self.router = router
        self.calls: list[tuple[str, str]] = []
        self.config = None

    async def complete(self, system: str, user: str, temperature=None, **_):
        self.calls.append((system, user))
        return self.router(system, user)


def judgment(
    *,
    gates=(True, True, True),
    dims=(8, 7, 7, 6, 6),
    topic="ai-materials",
    content_type="preprint",
) -> str:
    gate_ids = [gate.id for gate in PROFILE.definition.rubric.gates]
    dim_ids = [dim.id for dim in PROFILE.definition.rubric.dimensions]
    return json.dumps(
        {
            "content_type": content_type,
            "topic": topic,
            "gates": {g: {"passed": p, "reason": "mock"} for g, p in zip(gate_ids, gates)},
            "dimensions": {d: {"score": s, "reason": "mock"} for d, s in zip(dim_ids, dims)},
            "reason": "mock reason",
            "summary": "mock summary",
            "tags": ["mock"],
        }
    )


def make_item(
    title: str,
    url: str,
    content: str = MOCK_BODY,
    *,
    content_source: str = "feed_content",
    source_kind: str = "preprint",
    peer_review: str = "preprint",
    analysis: ContentAnalysis | None = None,
) -> ContentItem:
    return ContentItem(
        id=f"rss:mock:{abs(hash(url))}",
        source_type=SourceType.RSS,
        title=title,
        url=url,
        content=content,
        published_at=datetime(2026, 10, 9, 8, tzinfo=timezone.utc),
        fetched_at=NOW,
        profile="material-intel",
        metadata={
            "feed_name": "Mock feed",
            "content_source": content_source,
            "source_kind": source_kind,
            "peer_review": peer_review,
            "role": "primary_evidence",
        },
        processing=ProcessingResult(
            classification=ClassificationResult(profile="material-intel", method="source_override"),
            analysis=analysis,
        ),
    )


def analyzed(item: ContentItem, response: str) -> ContentItem:
    result, failure = ContentAnalyzer._validate_analysis_response(response, PROFILE)
    assert result is not None, failure
    item.processing.analysis = result
    return item


EVIDENCE_OK = {
    "material_system": "recycled polypropylene (rPP) blends from three suppliers",
    "data_scale": "48 formulations across 6 resin lots",
    "batches_or_lots": "6 resin lots, three suppliers",
    "conditions": "not reported",
    "baseline": "full factorial design (41 experiments)",
    "validation_method": "single extruder",
    "validation_setting": "lab",
    "independent_replication": "not reported",
    "event_date": "unknown",
    "claims": [
        {
            "claim": "Active learning reached the target in fewer experiments",
            "quote": "The loop reached the target melt flow index in 19 experiments",
            "location": "Results",
        }
    ],
    "results": ["target melt flow index reached in 19 experiments vs 41"],
    "limitations": ["validation used one extruder"],
    "reading_entry": "Results",
}


def artifact_json(language: str, *, extra: str = "") -> str:
    if language == "zh":
        blocks = {
            "why_read": "用主动学习选择再生 PP 配方，试验次数明显少于全因子设计。",
            "advance": "以高斯过程代理模型驱动的主动学习替代全因子设计来筛选再生 PP 共混配方。" + extra,
            "evidence": "来源报告覆盖三家供应商、6 个树脂批次、48 个配方；19 次实验达到目标熔指，全因子基线为 41 次。仅在一台挤出机上验证，属实验室环境。",
            "boundaries": "尚未展示跨设备或跨供应商的外推验证。",
        }
        title = "主动学习减少再生 PP 配方试验"
    else:
        blocks = {
            "why_read": "Active learning picked recycled-PP formulations with fewer trials than a full factorial design.",
            "advance": "A Gaussian-process active learning loop replaces full factorial screening of rPP blends." + extra,
            "evidence": "Three suppliers, 6 resin lots, 48 formulations; target melt flow index in 19 experiments versus 41 for the baseline. Lab validation on one extruder.",
            "boundaries": "No cross-equipment or cross-supplier validation is shown.",
        }
        title = "Active learning trims recycled-PP formulation trials"
    return json.dumps(
        {
            "title": title,
            "blocks": [
                {"id": block_id, "title": block_id, "content": text, "source_refs": []}
                for block_id, text in blocks.items()
            ],
        },
        ensure_ascii=False,
    )


def run(coro):
    return asyncio.run(coro)


# ---------------------------------------------------------- profile & rubric


def test_profile_declares_rubric_topics_and_no_search_tools():
    rubric = PROFILE.definition.rubric
    assert [d.id for d in rubric.dimensions] == [
        "relevance", "evidence", "transferability", "industrial", "novelty"
    ]
    assert [d.weight for d in rubric.dimensions] == [0.3, 0.25, 0.2, 0.15, 0.1]
    assert {g.id for g in rubric.gates} == {"domain_link", "new_information", "traceable"}
    assert [t.target_share for t in PROFILE.definition.topics] == [0.35, 0.3, 0.2, 0.15]
    # Search snippets must never stand in for reading the original.
    assert all(not block.tools for block in PROFILE.definition.enrichment.blocks)


def test_analysis_prompt_states_gates_floor_and_exclusions():
    prompt = analysis_system_prompt(PROFILE)
    assert "below 5 rejects the item regardless of other scores" in prompt
    assert "do not output an overall score" in prompt
    for phrase in ("leaderboards", "funding", "front-end"):
        assert phrase in prompt


def test_generic_hot_news_is_rejected_even_with_high_other_scores():
    item = analyzed(
        make_item("Why don't more developers use the platform?", "https://example.org/a"),
        judgment(gates=(False, True, True), dims=(2, 9, 9, 9, 9)),
    )
    analysis = item.processing.analysis
    assert analysis.track == "rejected"
    assert "gate:domain_link" in analysis.rejected_by
    assert "floor:relevance" in analysis.rejected_by


def test_low_relevance_cannot_be_compensated_by_other_dimensions():
    item = analyzed(
        make_item("Mock generic LLM benchmark", "https://example.org/b"),
        judgment(dims=(4.5, 10, 10, 10, 10)),
    )
    analysis = item.processing.analysis
    assert analysis.score == pytest.approx(8.35, abs=0.06)  # high weighted total ...
    assert analysis.track == "rejected"  # ... still rejected by the floor
    assert analysis.rejected_by == ["floor:relevance"]


def test_materials_research_is_admitted_to_main_track_with_reasons():
    item = analyzed(
        make_item("MOCK: Active learning for rPP", "https://example.org/c"),
        judgment(dims=(9, 7, 7, 6, 7)),
    )
    analysis = item.processing.analysis
    assert analysis.track == "main"
    assert analysis.score == pytest.approx(0.3 * 9 + 0.25 * 7 + 0.2 * 7 + 0.15 * 6 + 0.1 * 7, abs=0.06)
    assert set(analysis.dimensions) == {"relevance", "evidence", "transferability", "industrial", "novelty"}
    assert all(d.reason for d in analysis.dimensions.values())


def test_cross_domain_method_with_transfer_value_goes_to_exploration():
    item = analyzed(
        make_item("MOCK: Conformal prediction for drifting sensor data", "https://example.org/d"),
        judgment(dims=(6, 8, 9, 2, 8), topic="data-trust"),
    )
    analysis = item.processing.analysis
    assert analysis.track == "explore"
    assert analysis.topic == "data-trust"


def test_exploration_track_uses_its_own_bar(tmp_path, monkeypatch):
    orchestrator, _ = _orchestrator(tmp_path, monkeypatch, [], [])
    explore = analyzed(make_item("E", "https://example.org/e"), judgment(dims=(8, 6, 7, 3, 6)))
    assert explore.processing.analysis.track == "explore"
    assert 6.0 <= explore.processing.analysis.score < 6.5  # below the main threshold
    assert orchestrator.passes_profile_filter(explore)
    weak = analyzed(make_item("W", "https://example.org/w"), judgment(dims=(6, 5, 5, 2, 5)))
    assert weak.processing.analysis.track == "rejected" or not orchestrator.passes_profile_filter(weak)
    main_low = analyzed(make_item("M", "https://example.org/m"), judgment(dims=(7, 6, 6, 5, 6)))
    assert main_low.processing.analysis.track == "main"
    assert not orchestrator.passes_profile_filter(main_low)  # 6.2 < 6.5 for the main track


def test_missing_rubric_dimension_is_a_contract_failure():
    payload = json.loads(judgment())
    del payload["dimensions"]["evidence"]
    result, failure = ContentAnalyzer._validate_analysis_response(json.dumps(payload), PROFILE)
    assert result is None
    assert "missing dimension evidence" in failure


def test_unknown_topic_is_cleared_instead_of_invented():
    item = analyzed(make_item("MOCK", "https://example.org/e"), judgment(topic="quantum-gravity"))
    assert item.processing.analysis.topic is None


# ------------------------------------------------------------------ RSS


def _feed_client(text: str) -> AsyncMock:
    response = MagicMock()
    response.text = text
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    return client


SINCE = datetime(2026, 10, 8, tzinfo=timezone.utc)


def test_rss_prefers_full_content_and_decodes_entities():
    client = _feed_client((FIXTURES / "mixed_feed.xml").read_text())
    source = RSSSourceConfig(name="Mock", url="https://example.org/feed", profile="material-intel")
    items = run(RSSScraper([source], client).fetch(SINCE))
    by_title = {item.title: item for item in items}

    materials = by_title["MOCK: Active learning cuts formulation trials for recycled polypropylene blends"]
    assert materials.metadata["content_source"] == "feed_content"
    assert "19 experiments versus 41" in materials.content
    assert "<h2>" not in materials.content
    assert "Don't over-read" in materials.content
    # Double-encoded entity in the title is decoded once and for all.
    assert "Why don't more developers use the platform?" in by_title


def test_keyword_groups_drop_generic_news_before_any_ai_call():
    client = _feed_client((FIXTURES / "mixed_feed.xml").read_text())
    source = RSSSourceConfig(
        name="Mock",
        url="https://example.org/feed",
        keyword_groups=[["polymer", "polypropylene"], ["active learning", "machine learning"]],
    )
    titles = [item.title for item in run(RSSScraper([source], client).fetch(SINCE))]
    assert titles == ["MOCK: Active learning cuts formulation trials for recycled polypropylene blends"]


def test_old_items_are_not_reintroduced_as_new():
    client = _feed_client((FIXTURES / "mixed_feed.xml").read_text())
    source = RSSSourceConfig(name="Mock", url="https://example.org/feed", lookback_hours=120)
    titles = [item.title for item in run(RSSScraper([source], client).fetch(SINCE))]
    assert "MOCK: Old polymer machine learning post rediscovered" not in titles


def test_page_extraction_shorter_than_feed_keeps_feed_body():
    client = _feed_client((FIXTURES / "mixed_feed.xml").read_text())
    extractor = AsyncMock()
    extractor.extract.return_value = "Subscribe to read."
    registry = MagicMock()
    registry.get.return_value = extractor
    source = RSSSourceConfig(name="Mock", url="https://example.org/feed", content_extractor="x")
    items = run(RSSScraper([source], client, extractors=registry).fetch(SINCE))
    materials = next(item for item in items if item.title.startswith("MOCK: Active"))
    assert "19 experiments" in materials.content
    assert materials.metadata["content_source"] == "feed_content"


def test_failing_feed_is_reported_not_silently_empty():
    import httpx

    client = AsyncMock()
    client.get.side_effect = httpx.ConnectError("boom")
    source = RSSSourceConfig(name="Broken feed", url="https://example.org/feed")
    scraper = RSSScraper([source], client)
    assert run(scraper.fetch(SINCE)) == []
    assert scraper.source_failures and scraper.source_failures[0][0] == "Broken feed"


def test_html_challenge_page_counts_as_failure():
    client = _feed_client("<html><head><META NAME='robots'></head><body><p></html>")
    scraper = RSSScraper([RSSSourceConfig(name="Guarded", url="https://example.org/rss")], client)
    run(scraper.fetch(SINCE))
    assert scraper.source_failures


# ------------------------------------------------------- access & evidence


def test_summary_only_is_never_full_text():
    item = make_item("MOCK", "https://arxiv.org/abs/2610.00001v1", "A" * 1500, content_source="feed_summary")
    assert classify_access(item) == "abstract_or_summary"


def test_long_landing_page_without_sections_is_not_full_text_for_papers():
    item = make_item("MOCK", "https://example.org/paper", "word " * 1200, content_source="extracted_page")
    assert classify_access(item) == "abstract_or_summary"


def test_deep_read_upgrades_only_when_full_text_is_obtained():
    item = make_item("MOCK", "https://arxiv.org/abs/2610.00001v2", "Abstract text. " * 40, content_source="feed_summary")
    item.metadata["access_level"] = classify_access(item)
    paper = "Abstract\n" + "x " * 800 + "\n1 Introduction\n" + "y " * 800 + "\n2 Methods\n" + "z " * 800 + "\n3 Results\nok"
    extractor = AsyncMock()
    extractor.extract.return_value = paper
    registry = MagicMock()
    registry.get.return_value = extractor

    assert run(deep_read(item, registry, AsyncMock()))
    extractor.extract.assert_awaited_once()
    assert extractor.extract.await_args.args[0] == "https://arxiv.org/html/2610.00001"
    assert item.metadata["access_level"] == "full_text"
    assert item.metadata["fulltext_url"] == "https://arxiv.org/html/2610.00001"


def test_deep_read_failure_keeps_abstract_and_records_why():
    item = make_item("MOCK", "https://arxiv.org/abs/2610.00002", "Abstract text. " * 40, content_source="feed_summary")
    item.metadata["access_level"] = classify_access(item)
    extractor = AsyncMock()
    extractor.extract.return_value = None
    registry = MagicMock()
    registry.get.return_value = extractor
    assert not run(deep_read(item, registry, AsyncMock()))
    assert item.metadata["access_level"] == "abstract_or_summary"
    assert "not readable" in item.metadata["access_note"]


def test_evidence_record_does_not_fill_missing_numbers_or_trust_model_access_claims():
    item = make_item("MOCK", "https://example.org/x", MOCK_BODY, content_source="feed_summary")
    item.metadata["access_level"] = "abstract_or_summary"
    fabricated = dict(EVIDENCE_OK)
    fabricated.update(
        {
            "access_level": "full_text",  # model may not set code-owned fields
            "peer_review": "peer_reviewed",
            "data_scale": "1200 samples",  # number absent from the source
            "results": ["yield improved by 12%", "target reached in 19 experiments"],
            "claims": EVIDENCE_OK["claims"]
            + [{"claim": "cost fell", "quote": "costs fell by a third across plants", "location": "body"}],
        }
    )
    record = build_evidence_record(fabricated, item)
    assert record.access_level == "abstract_or_summary"
    assert record.peer_review == "preprint"
    assert record.data_scale == "not reported"
    assert record.results == ["target reached in 19 experiments"]
    assert [c.quote for c in record.claims] == [EVIDENCE_OK["claims"][0]["quote"]]
    assert record.checks["quotes_dropped"] == 1
    assert record.checks["kind"] == "citation_consistency"


def test_missing_fields_default_to_not_reported():
    item = make_item("MOCK", "https://example.org/y")
    record = build_evidence_record({"claims": []}, item)
    assert record.baseline == "not reported"
    assert record.validation_setting == "not reported"
    assert record.event_date == "unknown"
    assert record.independent_replication == "not reported"
    assert record.published_at == "2026-10-09"
    assert record.fetched_at == "2026-10-11"


# ------------------------------------------------------- writing checks


def _item_with_record() -> ContentItem:
    item = make_item("MOCK: Active learning for rPP", "https://example.org/rpp")
    item.processing.analysis = ContentAnalysis(score=7.5, reason="r", summary="s", track="main", topic="ai-materials")
    item.processing.evidence = build_evidence_record(EVIDENCE_OK, item)
    return item


def test_quality_check_flags_ungrounded_numbers_english_clauses_and_filler():
    from src.models import ContentBlock

    item = _item_with_record()
    blocks = [
        ContentBlock(id="advance", title="t", content="成本下降 30%，有望赋能行业。"),
        ContentBlock(id="evidence", title="t", content="This result was validated on one single extruder only today."),
    ]
    problems = artifact_quality_problems("标题", blocks, item, "zh")
    joined = " | ".join(problems)
    assert "30" in joined
    assert "有望赋能" in joined
    assert "untranslated English clause" in joined


def test_both_languages_are_written_from_one_shared_evidence_record():
    item = _item_with_record()
    zh_attempts = {"n": 0}

    def router(system: str, user: str) -> str:
        if "language tag `zh`" in system:
            zh_attempts["n"] += 1
            # First draft invents a cost figure; the validator forces a retry.
            return artifact_json("zh", extra="成本降低 30%。" if zh_attempts["n"] == 1 else "")
        return artifact_json("en")

    ai = ScriptedAI(router)
    enricher = ContentEnricher(ai, PROFILES, ["zh", "en"], console=Console(file=io.StringIO()))
    result = run(enricher.enrich_batch([item]))
    assert result.failed_count == 0
    assert zh_attempts["n"] == 2

    record_block = item.processing.evidence.model_dump_json(exclude={"checks"})
    evidence_sections = [
        user.split("# Evidence record", 1)[1].split("# Tool results", 1)[0]
        for _, user in ai.calls
        if "# Evidence record" in user
    ]
    assert len(set(evidence_sections)) == 1  # identical record in every language prompt

    def numbers(text):
        return set(re.findall(r"\d{2,}", text))

    allowed = numbers(record_block)
    for language in ("zh", "en"):
        artifact = item.processing.artifacts[language]
        text = artifact.title + " ".join(block.content for block in artifact.blocks)
        assert numbers(text) <= allowed
    zh_text = " ".join(b.content for b in item.processing.artifacts["zh"].blocks)
    en_text = " ".join(b.content for b in item.processing.artifacts["en"].blocks)
    assert numbers(zh_text) == numbers(en_text)
    assert "30" not in zh_text


def test_writing_fails_closed_when_model_keeps_inventing_numbers():
    item = _item_with_record()
    ai = ScriptedAI(lambda system, user: artifact_json("zh", extra="良率提升 15%。"))
    enricher = ContentEnricher(ai, PROFILES, ["zh"], console=Console(file=io.StringIO()))
    result = run(enricher.enrich_batch([item]))
    assert result.failed_count == 1
    assert "zh" not in item.processing.artifacts


def test_duplicate_sentences_and_sources_are_removed():
    first, second = dedupe_sentences(
        ["结果在三个批次上成立。主动学习减少了试验。", "结果在三个批次上成立。仍缺跨设备验证。"]
    )
    assert second == "仍缺跨设备验证。"
    sources = dedupe_sources(
        [
            ArtifactSource(id="1", title="Why don ’ t more developers ...", url="https://example.org/p?utm_source=x"),
            ArtifactSource(id="2", title="Duplicate", url="https://example.org/p"),
            ArtifactSource(id="3", title="Multiagent Systems - arXiv", url=""),
            ArtifactSource(id="4", title="Self link", url="https://example.org/item"),
        ],
        "https://example.org/item",
    )
    assert [(s.id, s.title) for s in sources] == [("1", "Why don’t more developers")]


def test_sentence_dedupe_keeps_decimals_intact():
    zh, en = dedupe_sentences(
        ["比值 1.81–1.95，重叠度由 0.57 升至 0.84。", "Ratios of 1.81–1.95 (mean 19.1%). Next sentence."]
    )
    assert zh == "比值 1.81–1.95，重叠度由 0.57 升至 0.84。"
    assert en == "Ratios of 1.81–1.95 (mean 19.1%). Next sentence."


def test_apostrophes_do_not_leave_html_entity_residue():
    escaped = _escape_markdown("Why don&#x27;t devs use it? It's fine")
    assert "&#x27;" not in escaped and "&\\#x27;" not in escaped
    assert "don't" in escaped and "It's" in escaped


# --------------------------------------------------------------- history


def test_history_keys_ignore_arxiv_versions_and_tracking():
    assert history_key("https://arxiv.org/abs/2610.00001v1") == history_key("http://arxiv.org/abs/2610.00001v3")
    assert history_key("https://example.org/a/?utm_source=x") == history_key("https://example.org/a")


def test_history_skips_items_seen_in_earlier_runs(tmp_path):
    history = RunHistory(tmp_path / "h.json")
    first = make_item("A", "https://arxiv.org/abs/2610.00001v1")
    history.record_items([first], "published", "2026-10-10")
    history.save()

    reloaded = RunHistory(tmp_path / "h.json")
    again = make_item("A v2", "https://arxiv.org/abs/2610.00001v2")
    fresh = make_item("B", "https://example.org/b")
    new, old = reloaded.split_unseen([again, fresh, make_item("B dup", "https://example.org/b/")])
    assert [item.title for item in new] == ["B"]
    assert len(old) == 2


# ----------------------------------------------------- end-to-end (mocked)


def _config(tmp_path: Path) -> Config:
    return Config(
        ai=AIConfig(provider="openai", model="mock", api_key_env="MOCK_KEY", languages=["zh", "en"]),
        sources=SourcesConfig(),
        collection=CollectionConfig(time_window_hours=48, history_path=str(tmp_path / "history.json")),
        digest=DigestConfig(renderer="research", track_limits={"main": 3, "explore": 1}, deep_read_limit=0),
        processing=ProcessingConfig(
            profiles_dir=str(ROOT / "profiles"),
            default_profile="material-intel",
            profile_settings={"material-intel": ProfileSettingsConfig(threshold=6.5, topic_dedup=False)},
        ),
    )


def _router(system: str, user: str) -> str:
    if system.startswith("# Evidence extraction"):
        return json.dumps(EVIDENCE_OK)
    if "# Target language" in system:
        return artifact_json("zh" if "language tag `zh`" in system else "en")
    if "Why don't more developers" in user:
        return judgment(gates=(False, True, True), dims=(1, 6, 3, 3, 5))
    if "MOCK: Active learning" in user:
        return judgment(dims=(9, 7, 7, 6, 7))
    return judgment(gates=(True, False, True), dims=(5, 3, 3, 3, 2))


def _orchestrator(tmp_path, monkeypatch, items, outcomes, router=_router):
    monkeypatch.chdir(tmp_path)
    config = _config(tmp_path)
    storage = StorageManager(data_dir=str(tmp_path / "data"))
    orchestrator = HorizonOrchestrator(config, storage, console=Console(file=io.StringIO()))
    ai = ScriptedAI(router)
    monkeypatch.setattr("src.orchestrator.create_ai_client", lambda _config: ai)

    async def fake_fetch(since):
        orchestrator.last_fetch_report = FetchReport(outcomes=outcomes)
        return [item.model_copy(deep=True) for item in items]

    orchestrator.fetch_all_sources = fake_fetch
    return orchestrator, ai


def _feed_items():
    materials = make_item("MOCK: Active learning for rPP", "https://example.org/rpp")
    generic = make_item("Why don't more developers use the platform?", "https://example.org/web", "Frameworks.", source_kind="news")
    for item in (materials, generic):
        item.processing = None
    return [materials, generic]


def test_research_run_publishes_grounded_bilingual_edition(tmp_path, monkeypatch):
    items = _feed_items()
    orchestrator, ai = _orchestrator(
        tmp_path, monkeypatch, items,
        [SourceFetchOutcome("RSS Feeds", "success", items=items)],
    )
    run(orchestrator.run())

    posts = sorted((tmp_path / "docs" / "_posts").glob("*.md"))
    assert [p.name[11:] for p in posts] == ["summary-en.md", "summary-zh.md"]  # legacy URL scheme kept
    zh = posts[1].read_text()
    assert '"edition": "research-radar"' in zh or 'edition: "research-radar"' in zh
    assert "主动学习减少再生 PP 配方试验" in zh
    assert "Why don" not in zh  # generic news never reaches the page
    # The mock body is short: it must be labelled abstract-level, not full text.
    assert "仅读到摘要" in zh and "已读全文" not in zh
    assert "引用一致性" in zh and "不是事实核验" in zh

    history = json.loads((tmp_path / "history.json").read_text())
    assert history["runs"][0]["status"] == "published"
    statuses = {entry["title"]: entry["status"] for entry in history["items"].values()}
    assert statuses["MOCK: Active learning for rPP"] == "published"
    assert statuses["Why don't more developers use the platform?"] == "screened"

    # Re-running the same day neither overwrites the issue nor re-analyzes.
    calls_before = len(ai.calls)
    run(orchestrator.run())
    history = json.loads((tmp_path / "history.json").read_text())
    assert history["runs"][0]["status"] == "already_published"
    assert len(ai.calls) == calls_before


def test_no_qualified_content_is_distinct_from_source_failure(tmp_path, monkeypatch):
    generic = _feed_items()[1:]
    orchestrator, _ = _orchestrator(
        tmp_path, monkeypatch, generic,
        [SourceFetchOutcome("RSS Feeds", "success", items=generic)],
    )
    run(orchestrator.run())
    history = json.loads((tmp_path / "history.json").read_text())
    assert history["runs"][0]["status"] == "no_qualified"
    assert not (tmp_path / "docs" / "_posts").exists() or not list((tmp_path / "docs" / "_posts").glob("*.md"))

    failing, _ = _orchestrator(
        tmp_path, monkeypatch, [],
        [SourceFetchOutcome("RSS Feeds", "failure", error="ConnectError", failed_feeds=["Feed A", "Feed B"])],
    )
    with pytest.raises(RuntimeError):
        run(failing.run())
    history = json.loads((tmp_path / "history.json").read_text())
    assert history["runs"][0]["status"] == "source_failure"
    assert history["runs"][0]["failed_sources"] == ["Feed A", "Feed B"]
    assert history["runs"][1]["status"] == "no_qualified"


def test_partial_source_failure_is_published_with_a_visible_warning(tmp_path, monkeypatch):
    items = _feed_items()
    orchestrator, _ = _orchestrator(
        tmp_path, monkeypatch, items,
        [SourceFetchOutcome("RSS Feeds", "success", items=items, error="x", failed_feeds=["Feed C"])],
    )
    run(orchestrator.run())
    zh = (tmp_path / "docs" / "_posts").glob("*-summary-zh.md").__next__().read_text()
    assert "1 个来源采集失败（Feed C）" in zh
    history = json.loads((tmp_path / "history.json").read_text())
    assert history["runs"][0]["status"] == "published_degraded"


def test_ai_outage_is_a_processing_failure_not_an_empty_day(tmp_path, monkeypatch):
    items = _feed_items()

    def broken(system, user):
        raise RuntimeError("401 invalid key")

    orchestrator, _ = _orchestrator(
        tmp_path, monkeypatch, items,
        [SourceFetchOutcome("RSS Feeds", "success", items=items)],
        router=broken,
    )
    monkeypatch.setattr("src.ai.analyzer.ContentAnalyzer._analyze_item.retry.wait", lambda *_: 0, raising=False)
    with pytest.raises(RuntimeError, match="AI processing failed"):
        run(orchestrator.run())
    history = json.loads((tmp_path / "history.json").read_text())
    assert history["runs"][0]["status"] == "processing_failure"
    assert history["items"] == {}  # nothing recorded, so a rerun retries everything


def test_track_limits_are_caps_not_quotas(tmp_path, monkeypatch):
    orchestrator, _ = _orchestrator(tmp_path, monkeypatch, [], [])
    main = [
        analyzed(make_item(f"M{i}", f"https://example.org/m{i}"), judgment(dims=(9, 8, 7, 6, 6)))
        for i in range(5)
    ]
    explore = [
        analyzed(make_item(f"E{i}", f"https://example.org/e{i}"), judgment(dims=(7, 8, 9, 1, 8)))
        for i in range(3)
    ]
    kept = orchestrator.apply_track_limits(main + explore)
    assert [i.title for i in kept] == ["M0", "M1", "M2", "E0"]
    assert orchestrator.apply_track_limits([]) == []


# ------------------------------------------------------------- rendering


def test_renderer_marks_abstract_only_and_escapes_untrusted_text():
    item = _item_with_record()
    item.title = 'MOCK <script>alert("x")</script>'
    item.metadata["access_level"] = "abstract_or_summary"
    item.processing.evidence.access_level = "abstract_or_summary"
    from src.models import ContentArtifact, ContentBlock

    item.processing.artifacts["zh"] = ContentArtifact(
        language="zh",
        title="标题 <b>x</b>",
        blocks=[
            ContentBlock(id="why_read", title="w", content="值得读 it's", primary=True),
            ContentBlock(id="advance", title="a", content="新增"),
            ContentBlock(id="boundaries", title="b", content="边界"),
        ],
    )
    edition = ResearchEditionRenderer(PROFILE.definition.topics).render(
        [item], "2026-10-11", "zh", EditionStats(fetched=10, new=5, screened=5)
    )
    text = edition.post_text()
    assert "仅读到摘要" in text and "已读全文" not in text
    # Body HTML is escaped; front matter keeps raw data that templates escape.
    assert "<script>" not in edition.body and "<b>x</b>" not in edition.body
    assert "标题 &lt;b&gt;x&lt;/b&gt;" in edition.body
    assert "&#x27;" in text or "it&#x27;s" in text or "it's" in text
    assert "&\\#x27;" not in text
    assert "未报告" in text  # conditions were not reported
    assert edition.front_matter["picks"][0]["access"] == "abstract_or_summary"
    assert edition.front_matter["picks"][0]["topic_name"] == "AI × 材料与聚合物研发"
    assert 'href="https://example.org/rpp"' in text


def test_metadata_numbers_cannot_ground_performance_claims():
    from src.models import ContentBlock

    item = _item_with_record()
    item.processing.evidence.access_note = "Fetched 98765 characters"
    item.processing.evidence.checks["attempts"] = 54321
    blocks = [ContentBlock(id="evidence", title="Evidence", content="Accuracy improved by 2026%, with 98765 samples and 54321 trials.")]
    problems = " ".join(artifact_quality_problems("MOCK result", blocks, item, "en"))
    assert all(number in problems for number in ("2026", "98765", "54321"))


def test_valid_quote_does_not_ground_invented_claim_or_limitation_numbers():
    item = make_item("MOCK study", "https://example.org/mock", content="The model was evaluated on held-out batches.")
    record = build_evidence_record({
        "claims": [{"claim": "Accuracy reached 99.99%", "quote": "The model was evaluated on held-out batches.", "location": "body"}],
        "limitations": ["Only 98765 samples were tested", "not addressed: independent replication"],
    }, item)
    assert record.claims == []
    assert record.limitations == ["not addressed: independent replication"]
    assert record.checks["claims_dropped_ungrounded_numbers"] == 1
    assert record.checks["limitations_dropped_ungrounded_numbers"] == 1


@pytest.mark.parametrize("language,heading", [("zh", "本期阅读指南"), ("en", "Reading guide")])
def test_reading_guide_links_match_cards_and_empty_editions_omit_guide(language, heading):
    renderer = ResearchEditionRenderer(PROFILE.definition.topics)
    main = _item_with_record()
    explore = _item_with_record()
    explore.processing.analysis.track = "explore"
    edition = renderer.render([main, explore], "2026-10-11", language, EditionStats())
    assert heading in edition.body
    for pick in edition.front_matter["picks"]:
        assert f'href="#{pick["anchor"]}"' in edition.body
        assert f'id="{pick["anchor"]}"' in edition.body
    assert 'class="reading-guide"' not in renderer.render([], "2026-10-11", language, EditionStats()).body
