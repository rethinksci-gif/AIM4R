"""Prompt construction for profile-driven content analysis."""

import json

from ...models import ContentItem
from ...processing.profiles import LoadedProfile, ProfileRubric
from .common import EVIDENCE_RULES, UNTRUSTED_INPUT_RULE

ANALYSIS_RULES = f"""You are a content curator evaluating an item under the supplied processing profile.

- {UNTRUSTED_INPUT_RULE}
- Base the analysis only on the supplied item and its metadata.
{EVIDENCE_RULES}
- Apply the profile's evaluation policy consistently."""


def _rubric_contract(profile: LoadedProfile, rubric: ProfileRubric) -> str:
    gates = "\n".join(f"- `{gate.id}`: {gate.description}" for gate in rubric.gates)
    dimensions = "\n".join(
        f"- `{dimension.id}` (weight {dimension.weight:.0%}"
        + (
            f"; below {dimension.min_score:g} rejects the item regardless of other scores"
            if dimension.min_score is not None
            else ""
        )
        + f"): {dimension.description}"
        for dimension in rubric.dimensions
    )
    topics = profile.definition.topics
    topic_line = (
        "\n  \"topic\": \"<one of: "
        + ", ".join(topic.id for topic in topics)
        + ", or null when none fits>\","
        if topics
        else ""
    )
    content_types = (
        "<one of: " + ", ".join(rubric.content_types) + ">"
        if rubric.content_types
        else "<short content type>"
    )
    example = {
        "gates": {gate.id: {"passed": True, "reason": "..."} for gate in rubric.gates},
        "dimensions": {
            dimension.id: {"score": 0, "reason": "..."}
            for dimension in rubric.dimensions
        },
    }
    rubric_json = json.dumps(example, indent=2)[1:-1].strip()
    return f"""# Selection rubric

Step 1 — admission gates. Judge each gate independently with a one-sentence reason. Failing any gate rejects the item.
{gates}

Step 2 — dimensions. Score each dimension 0-10 with a one-sentence reason that cites what in the item supports the score. Do not let brand recognition, likes, stars or community heat stand in for technical value.
{dimensions}

The engine computes the weighted total; do not output an overall score.

# Output contract

Return valid JSON only:
{{
  "content_type": "{content_types}",{topic_line}
  {rubric_json},
  "reason": "<one sentence: why a reader should or should not read the original>",
  "summary": "<one-sentence factual summary of what the item reports>",
  "tags": ["<tag>", "..."]
}}"""


def analysis_system_prompt(profile: LoadedProfile) -> str:
    rubric = profile.definition.rubric
    if rubric is not None:
        return f"""{ANALYSIS_RULES}

# Profile policy

{profile.analysis_prompt}

{_rubric_contract(profile, rubric)}"""
    return f"""{ANALYSIS_RULES}

# Profile policy

{profile.analysis_prompt}

# Output contract

Return valid JSON only:
{{
  "score": <number from 0 to 10>,
  "reason": "<concise explanation>",
  "summary": "<one-sentence summary>",
  "tags": ["<tag>", "..."]
}}"""


def source_context_lines(item: ContentItem) -> str:
    """Describe source nature and how much of the original was available."""
    meta = item.metadata
    lines = []
    if meta.get("feed_name"):
        lines.append(f"Feed: {meta['feed_name']}")
    for key, label in (
        ("source_kind", "Source kind"),
        ("role", "Source role"),
        ("peer_review", "Peer review status (from source config)"),
        ("access_level", "Access level"),
        ("content_source", "Content obtained from"),
    ):
        if meta.get(key):
            lines.append(f"{label}: {meta[key]}")
    lines.append(f"Published: {item.published_at.date().isoformat()}")
    return "\n".join(lines)


def analysis_user_prompt(
    item: ContentItem,
    content_section: str,
    discussion_section: str,
) -> str:
    return f"""Analyze the following content.

Title: {item.title}
Source: {item.source_type.value}
Author: {item.author or "Unknown"}
URL: {item.url}
{source_context_lines(item)}
{content_section}
{discussion_section}"""
