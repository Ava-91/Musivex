"""Conservative reverb signal detection."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ReverbResult:
    score: float
    detected: bool
    confidence: float


def detect_reverb(decay_score: float, *, threshold: float = 0.55) -> ReverbResult:
    score = max(0.0, min(1.0, decay_score))
    detected = score >= threshold
    confidence = abs(score - threshold) / max(threshold, 1e-9)
    return ReverbResult(score, detected, min(1.0, confidence))
