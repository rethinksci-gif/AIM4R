"""Render the evidence-first research edition as Jekyll posts.

Cards are emitted as HTML so untrusted text never goes through Markdown
escaping. Every value is HTML-escaped; only http(s) links are emitted.
"""

import html
import json
from dataclasses import dataclass, field
from typing import Any, Optional
from urllib.parse import urlsplit

from .localization import normalize_language
from ..models import ContentItem, EvidenceRecord
from ..processing.profiles import ProfileTopic

LABELS: dict[str, dict[str, Any]] = {
    "zh": {
        "title": "AIM4R 研究雷达 · {date}",
        "lede": "本期精选 {selected} 条，来自 {new} 条新内容（本轮共采集 {fetched} 条）。",
        "lede_explore": "其中 {explore} 条列入探索栏目。",
        "degraded": "注意：本次有 {count} 个来源采集失败（{names}），覆盖可能不完整。",
        "empty": "本次没有达到入选标准的内容（已筛查 {screened} 条新内容）。没有凑数。",
        "explore_heading": "探索栏目",
        "explore_note": "研究价值较高、但离工业应用尚远的内容。",
        "other_topic": "其他相关",
        "read_original": "阅读原文",
        "fulltext": "已读全文版本",
        "published": "发布",
        "fetched": "收录",
        "event": "事件日期",
        "why": "为什么值得读",
        "evidence_record": "证据记录",
        "evidence_hint": "字段与摘录保留原文语言，按来源报告填写。",
        "quotes": "原文摘录",
        "references": "辅助引用（搜索线索，未逐条核验）",
        "check_note": "自动检查（引用一致性，不是事实核验）：{kept} 条摘录可在已读文本中定位{dropped}。",
        "check_dropped": "，{count} 条无法定位已删除",
        "not_reported": "未报告",
        "unknown": "未知",
        "blocks": {
            "advance": "新增进展",
            "evidence": "关键证据",
            "significance": "研发意义",
            "boundaries": "适用边界",
            "next_step": "下一步",
        },
        "fields": {
            "material_system": "材料体系",
            "data_scale": "数据规模",
            "batches_or_lots": "批次/批号",
            "conditions": "条件",
            "baseline": "比较基线",
            "validation_method": "验证方法",
            "validation_setting": "验证环境",
            "independent_replication": "独立复现",
            "event_date": "事件日期",
        },
        "access": {
            "full_text": "已读全文",
            "abstract_or_summary": "仅读到摘要",
            "snippet": "仅片段",
            "title_only": "仅标题",
        },
        "source_kind": {
            "preprint": "预印本",
            "journal": "期刊论文",
            "lab_blog": "研究机构/企业研究博客",
            "institutional": "研究机构发布",
            "vendor": "厂商内容",
            "trade_press": "行业媒体",
            "news": "新闻",
            "code": "开源代码",
            "commentary": "评论分析",
        },
        "peer_review": {
            "peer_reviewed": "同行评审",
            "preprint": "未经同行评审",
            "unknown": "评审状态未知",
        },
        "role": {
            "primary_evidence": "原始证据",
            "discovery": "发现线索",
            "commentary": "评论分析",
        },
        "validation_setting": {
            "simulation": "仿真",
            "lab": "实验室",
            "pilot": "中试",
            "production": "生产",
            "mixed": "混合",
        },
    },
    "en": {
        "title": "AIM4R Research Radar · {date}",
        "lede": "{selected} picks this edition, from {new} new items ({fetched} collected).",
        "lede_explore": "{explore} of them are in the Exploration track.",
        "degraded": "Note: {count} source(s) failed this run ({names}); coverage may be incomplete.",
        "empty": "Nothing met the bar this run ({screened} new items screened). No filler added.",
        "explore_heading": "Exploration",
        "explore_note": "High research value, still far from industrial use.",
        "other_topic": "Also relevant",
        "read_original": "Read the original",
        "fulltext": "Full-text version read",
        "published": "Published",
        "fetched": "Collected",
        "event": "Event date",
        "why": "Why read it",
        "evidence_record": "Evidence record",
        "evidence_hint": "Fields and excerpts are kept in the source language, as reported by the source.",
        "quotes": "Excerpts from the source",
        "references": "Supporting links (search leads, not individually verified)",
        "check_note": "Automatic check (citation consistency, not fact verification): {kept} excerpt(s) located in the text that was read{dropped}.",
        "check_dropped": "; {count} could not be located and were removed",
        "not_reported": "not reported",
        "unknown": "unknown",
        "blocks": {
            "advance": "What's new",
            "evidence": "Key evidence",
            "significance": "Why it matters for R&D",
            "boundaries": "Limits",
            "next_step": "Next step",
        },
        "fields": {
            "material_system": "Material system",
            "data_scale": "Data scale",
            "batches_or_lots": "Batches / lots",
            "conditions": "Conditions",
            "baseline": "Baseline",
            "validation_method": "Validation method",
            "validation_setting": "Validation setting",
            "independent_replication": "Independent replication",
            "event_date": "Event date",
        },
        "access": {
            "full_text": "Full text read",
            "abstract_or_summary": "Abstract only",
            "snippet": "Snippet only",
            "title_only": "Title only",
        },
        "source_kind": {
            "preprint": "Preprint",
            "journal": "Journal article",
            "lab_blog": "Research lab blog",
            "institutional": "Institutional release",
            "vendor": "Vendor content",
            "trade_press": "Trade press",
            "news": "News",
            "code": "Open-source code",
            "commentary": "Commentary",
        },
        "peer_review": {
            "peer_reviewed": "Peer reviewed",
            "preprint": "Not peer reviewed",
            "unknown": "Review status unknown",
        },
        "role": {
            "primary_evidence": "Primary evidence",
            "discovery": "Discovery lead",
            "commentary": "Commentary",
        },
        "validation_setting": {
            "simulation": "Simulation",
            "lab": "Lab",
            "pilot": "Pilot",
            "production": "Production",
            "mixed": "Mixed",
        },
    },
}

BLOCK_ORDER = ("advance", "evidence", "significance", "boundaries", "next_step")


@dataclass
class EditionStats:
    fetched: int = 0
    new: int = 0
    screened: int = 0
    failed_sources: list[str] = field(default_factory=list)


@dataclass
class RenderedEdition:
    title: str
    front_matter: dict[str, Any]
    body: str

    def post_text(self) -> str:
        lines = ["---"]
        for key, value in self.front_matter.items():
            lines.append(f"{key}: {_yaml_value(value)}")
        lines.append("---")
        return "\n".join(lines) + "\n\n" + self.body


def _yaml_value(value: Any) -> str:
    # JSON is a subset of YAML 1.2 flow syntax and is unambiguous for strings.
    return json.dumps(value, ensure_ascii=False)


def _e(value: object) -> str:
    return html.escape(str(value), quote=True)


def _safe_href(url: Optional[str]) -> Optional[str]:
    if not url:
        return None
    raw = str(url).strip()
    try:
        parsed = urlsplit(raw)
    except ValueError:
        return None
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
        return None
    if any(ord(char) < 32 for char in raw):
        return None
    return _e(raw)


def _date_label(iso: Optional[str], language: str) -> str:
    if not iso:
        return ""
    year, month, day = iso.split("-")
    if language == "zh":
        return f"{int(month)}月{int(day)}日"
    return f"{year}-{month}-{day}"


class ResearchEditionRenderer:
    """Builds the research-radar post for one language."""

    def __init__(self, topics: list[ProfileTopic]):
        self.topics = topics

    def topic_name(self, topic_id: Optional[str], language: str) -> str:
        labels = LABELS.get(language, LABELS["en"])
        for topic in self.topics:
            if topic.id == topic_id:
                return topic.names.get(language) or topic.names.get("en") or topic.id
        return labels["other_topic"]

    def render(
        self,
        items: list[ContentItem],
        date: str,
        language: str,
        stats: EditionStats,
        *,
        status: str = "published",
    ) -> RenderedEdition:
        labels = LABELS.get(language, LABELS["en"])
        title = labels["title"].format(date=date)
        main = [item for item in items if _track(item) != "explore"]
        explore = [item for item in items if _track(item) == "explore"]

        lede = labels["lede"].format(selected=len(items), new=stats.new, fetched=stats.fetched)
        if explore:
            lede += ("" if language == "zh" else " ") + labels["lede_explore"].format(
                explore=len(explore)
            )
        if not items:
            lede = labels["empty"].format(screened=stats.screened)

        parts = [f'<p class="issue-lede">{_e(lede)}</p>']
        if stats.failed_sources:
            parts.append(
                '<p class="issue-warning" role="note">'
                + _e(
                    labels["degraded"].format(
                        count=len(stats.failed_sources),
                        names=", ".join(stats.failed_sources),
                    )
                )
                + "</p>"
            )

        picks = []
        index = 0
        for topic_id, group in self._group_by_topic(main):
            parts.append(
                f'<h2 id="topic-{_e(topic_id or "other")}">{_e(self.topic_name(topic_id, language))}</h2>'
            )
            for item in group:
                index += 1
                parts.append(self._card(item, index, language))
                picks.append(self._pick_summary(item, index, language))
        if explore:
            parts.append(f'<h2 id="explore">{_e(labels["explore_heading"])}</h2>')
            parts.append(f'<p class="track-note">{_e(labels["explore_note"])}</p>')
            for item in explore:
                index += 1
                parts.append(self._card(item, index, language))
                picks.append(self._pick_summary(item, index, language))

        front_matter = {
            "layout": "default",
            "title": title,
            "date": date,
            "lang": language,
            "edition": "research-radar",
            "issue_status": status,
            "description": lede,
            "picks_count": len(items),
            "failed_sources": stats.failed_sources,
            "picks": picks,
        }
        body = normalize_language("\n\n".join(parts) + "\n", language)
        front_matter = json.loads(
            normalize_language(json.dumps(front_matter, ensure_ascii=False), language)
        )
        return RenderedEdition(title=title, front_matter=front_matter, body=body)

    def _group_by_topic(
        self, items: list[ContentItem]
    ) -> list[tuple[Optional[str], list[ContentItem]]]:
        order = {topic.id: position for position, topic in enumerate(self.topics)}
        groups: dict[Optional[str], list[ContentItem]] = {}
        for item in items:
            groups.setdefault(_topic(item), []).append(item)
        return sorted(groups.items(), key=lambda pair: order.get(pair[0], len(order)))

    def _pick_summary(self, item: ContentItem, index: int, language: str) -> dict[str, Any]:
        artifact = item.processing.artifacts.get(language) if item.processing else None
        why = _block(artifact, "why_read")
        evidence = item.processing.evidence if item.processing else None
        return {
            "anchor": f"pick-{index}",
            "title": artifact.title if artifact else item.title,
            "why": why,
            "topic": _topic(item) or "other",
            "topic_name": self.topic_name(_topic(item), language),
            "track": _track(item),
            "source_kind": item.metadata.get("source_kind") or "unknown",
            "access": (evidence.access_level if evidence else item.metadata.get("access_level"))
            or "unknown",
            "url": str(item.url),
        }

    def _badges(self, item: ContentItem, evidence: Optional[EvidenceRecord], language: str) -> str:
        labels = LABELS.get(language, LABELS["en"])
        badges = []
        kind = item.metadata.get("source_kind") or (
            "code" if item.source_type.value == "github" else None
        )
        if kind:
            badges.append(("kind", kind, labels["source_kind"].get(kind, kind)))
        role = item.metadata.get("role")
        if role and role != "primary_evidence":
            badges.append(("role", role, labels["role"].get(role, role)))
        access = evidence.access_level if evidence else item.metadata.get("access_level")
        if access:
            badges.append(("access", access, labels["access"].get(access, access)))
        review = evidence.peer_review if evidence else item.metadata.get("peer_review")
        if review and review != "not_applicable" and review != "unknown":
            badges.append(("review", review, labels["peer_review"].get(review, review)))
        return "".join(
            f'<span class="badge" data-kind="{_e(kind_)}" data-value="{_e(value)}">{_e(text)}</span>'
            for kind_, value, text in badges
        )

    def _card(self, item: ContentItem, index: int, language: str) -> str:
        labels = LABELS.get(language, LABELS["en"])
        artifact = item.processing.artifacts.get(language) if item.processing else None
        evidence = item.processing.evidence if item.processing else None
        title = artifact.title if artifact else item.title
        href = _safe_href(str(item.url))

        meta_bits = [_e(item.metadata.get("feed_name") or item.author or "")]
        if evidence:
            meta_bits.append(f'{_e(labels["published"])} {_e(_date_label(evidence.published_at, language))}')
            if evidence.event_date not in ("unknown", "", None) and evidence.event_date != evidence.published_at:
                meta_bits.append(f'{_e(labels["event"])} <span lang="en">{_e(evidence.event_date)}</span>')
            meta_bits.append(f'{_e(labels["fetched"])} {_e(_date_label(evidence.fetched_at, language))}')
        else:
            meta_bits.append(
                f'{_e(labels["published"])} {_e(_date_label(item.published_at.date().isoformat(), language))}'
            )
        meta_line = " · ".join(bit for bit in meta_bits if bit)

        actions = []
        if href:
            actions.append(f'<a class="read-original" href="{href}">{_e(labels["read_original"])} ↗</a>')
        fulltext = _safe_href(item.metadata.get("fulltext_url"))
        if fulltext and item.metadata.get("fulltext_url") != str(item.url):
            actions.append(f'<a class="read-fulltext" href="{fulltext}">{_e(labels["fulltext"])} ↗</a>')

        lines = [
            f'<article class="pick" id="pick-{index}" data-track="{_e(_track(item))}">',
            f'<p class="pick-badges">{self._badges(item, evidence, language)}</p>',
            f"<h3>{_e(title)}</h3>",
        ]
        why = _block(artifact, "why_read")
        if why:
            lines.append(
                f'<p class="pick-why"><span class="label">{_e(labels["why"])}</span>{_e(why)}</p>'
            )
        lines.append(f'<p class="pick-actions">{"".join(actions)}<span class="pick-meta">{meta_line}</span></p>')
        if artifact:
            lines.append('<div class="pick-body">')
            by_id = {block.id: block for block in artifact.blocks}
            for block_id in BLOCK_ORDER:
                block = by_id.get(block_id)
                if block is None or not block.content.strip():
                    continue
                heading = labels["blocks"].get(block_id, block.title)
                lines.append(f'<h4 data-block="{_e(block_id)}">{_e(heading)}</h4>')
                lines.append(f"<p>{_e(block.content)}</p>")
            lines.append("</div>")
        if evidence:
            lines.append(self._evidence_panel(evidence, language))
        sources = artifact.sources if artifact else []
        links = [
            f'<li><a href="{_safe_href(source.url)}">{_e(source.title)}</a></li>'
            for source in sources
            if _safe_href(source.url)
        ]
        if links:
            lines.append(
                f'<details class="pick-references"><summary>{_e(labels["references"])}</summary><ul>'
                + "".join(links)
                + "</ul></details>"
            )
        lines.append("</article>")
        return "\n".join(lines)

    def _evidence_panel(self, evidence: EvidenceRecord, language: str) -> str:
        labels = LABELS.get(language, LABELS["en"])
        rows = []
        for field_id, label in labels["fields"].items():
            value = getattr(evidence, field_id)
            if field_id == "validation_setting":
                text = labels["validation_setting"].get(value)
                if text:
                    rows.append(f"<dt>{_e(label)}</dt><dd>{_e(text)}</dd>")
                    continue
            if value in ("not reported", "", None):
                rows.append(f'<dt>{_e(label)}</dt><dd class="missing">{_e(labels["not_reported"])}</dd>')
            elif value == "unknown":
                rows.append(f'<dt>{_e(label)}</dt><dd class="missing">{_e(labels["unknown"])}</dd>')
            elif value == "reported":
                rows.append(f"<dt>{_e(label)}</dt><dd>✓</dd>")
            else:
                rows.append(f'<dt>{_e(label)}</dt><dd lang="en">{_e(value)}</dd>')
        quotes = "".join(
            f'<li><q lang="en">{_e(claim.quote)}</q> <span class="quote-loc" lang="en">— {_e(claim.location)}</span></li>'
            for claim in evidence.claims
        )
        checks = evidence.checks or {}
        dropped = checks.get("quotes_dropped") or 0
        note = labels["check_note"].format(
            kept=checks.get("quotes_kept", len(evidence.claims)),
            dropped=labels["check_dropped"].format(count=dropped) if dropped else "",
        )
        parts = [
            f'<details class="pick-evidence"><summary>{_e(labels["evidence_record"])}</summary>',
            f'<p class="evidence-hint">{_e(labels["evidence_hint"])}</p>',
            f"<dl>{''.join(rows)}</dl>",
        ]
        if quotes:
            parts.append(f'<p class="evidence-sub">{_e(labels["quotes"])}</p><ol class="quotes">{quotes}</ol>')
        parts.append(f'<p class="check-note">{_e(note)}</p>')
        parts.append("</details>")
        return "".join(parts)


def _track(item: ContentItem) -> str:
    analysis = item.processing.analysis if item.processing else None
    return (analysis.track if analysis and analysis.track else None) or "main"


def _topic(item: ContentItem) -> Optional[str]:
    analysis = item.processing.analysis if item.processing else None
    return analysis.topic if analysis else None


def _block(artifact, block_id: str) -> str:
    if not artifact:
        return ""
    for block in artifact.blocks:
        if block.id == block_id:
            return block.content.strip()
    return ""
