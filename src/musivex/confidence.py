"""Confidence scoring and review decisions."""

from dataclasses import dataclass
from enum import StrEnum


class MatchDecision(StrEnum):
    AUTO = "auto"
    REVIEW = "review"
    REJECT = "reject"


@dataclass(frozen=True, slots=True)
class MatchAssessment:
    score: float
    decision: MatchDecision
    reason: str


def assess(score: float, *, auto_threshold: float = 0.90, review_threshold: float = 0.65) -> MatchAssessment:
    if not 0 <= score <= 1:
        raise ValueError("score must be between 0 and 1")
    if score >= auto_threshold:
        return MatchAssessment(score, MatchDecision.AUTO, "high-confidence match")
    if score >= review_threshold:
        return MatchAssessment(score, MatchDecision.REVIEW, "ambiguous match requires review")
    return MatchAssessment(score, MatchDecision.REJECT, "confidence below review threshold")
