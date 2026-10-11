"""Deterministic evaluation of profile rubrics.

The model judges each gate and dimension with a reason; this module turns
those judgments into a weighted score, a track and an explicit rejection
list. Low relevance cannot be compensated by other dimensions because floors
are checked before the weighted sum is used.
"""

from typing import Any, Optional

from ..models import ContentAnalysis, RubricDimensionResult, RubricGateResult
from .profiles import ProfileRubric


class RubricContractError(ValueError):
    """Raised when a model response does not cover the declared rubric."""


def parse_rubric_fields(parsed: dict[str, Any], rubric: ProfileRubric) -> dict[str, Any]:
    """Validate rubric fields in a raw analysis response.

    Returns keyword arguments for ``ContentAnalysis`` with gates, dimensions,
    content type and topic normalized. Raises ``RubricContractError`` when a
    declared gate or dimension is missing.
    """
    raw_gates = parsed.get("gates") or {}
    raw_dimensions = parsed.get("dimensions") or {}
    if not isinstance(raw_gates, dict) or not isinstance(raw_dimensions, dict):
        raise RubricContractError("gates and dimensions must be JSON objects")

    gates: dict[str, RubricGateResult] = {}
    for gate in rubric.gates:
        value = raw_gates.get(gate.id)
        if value is None:
            raise RubricContractError(f"missing gate {gate.id}")
        if isinstance(value, bool):
            value = {"passed": value}
        gates[gate.id] = RubricGateResult.model_validate(value)

    dimensions: dict[str, RubricDimensionResult] = {}
    for dimension in rubric.dimensions:
        value = raw_dimensions.get(dimension.id)
        if value is None:
            raise RubricContractError(f"missing dimension {dimension.id}")
        if isinstance(value, (int, float)):
            value = {"score": value}
        dimensions[dimension.id] = RubricDimensionResult.model_validate(value)

    content_type = parsed.get("content_type")
    if rubric.content_types and content_type not in rubric.content_types:
        content_type = "other"
    return {
        "gates": gates,
        "dimensions": dimensions,
        "content_type": content_type,
        "topic": parsed.get("topic") or None,
    }


def apply_rubric(
    analysis: ContentAnalysis,
    rubric: ProfileRubric,
    *,
    topic_ids: Optional[set[str]] = None,
) -> ContentAnalysis:
    """Compute score, track and rejection reasons from rubric judgments."""
    rejected_by = [
        f"gate:{gate.id}"
        for gate in rubric.gates
        if not analysis.gates.get(gate.id, RubricGateResult(passed=False)).passed
    ]
    total = 0.0
    for dimension in rubric.dimensions:
        result = analysis.dimensions.get(dimension.id)
        score = result.score if result else 0.0
        total += dimension.weight * score
        if dimension.min_score is not None and score < dimension.min_score:
            rejected_by.append(f"floor:{dimension.id}")

    analysis.score = round(total, 1)
    analysis.rejected_by = rejected_by
    if topic_ids is not None and analysis.topic not in topic_ids:
        analysis.topic = None

    if rejected_by:
        analysis.track = "rejected"
    elif rubric.explore and _routes_to_explore(analysis, rubric):
        analysis.track = "explore"
    else:
        analysis.track = "main"
    return analysis


def _routes_to_explore(analysis: ContentAnalysis, rubric: ProfileRubric) -> bool:
    rule = rubric.explore
    result = analysis.dimensions.get(rule.dimension)
    if result is None or result.score >= rule.below:
        return False
    return rule.min_total is None or (analysis.score or 0) >= rule.min_total
