"""Safety decision for recognition results."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ReviewDecision:
    apply_automatically: bool
    requires_review: bool
    reason: str


def decide(confidence: float, threshold: float) -> ReviewDecision:
    if confidence >= threshold:
        return ReviewDecision(True, False, "confidence meets threshold")
    return ReviewDecision(False, True, "confidence below threshold")
