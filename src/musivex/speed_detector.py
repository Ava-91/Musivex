"""Detect time-scale transformations from reference comparison signals."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SpeedResult:
    ratio: float
    slowed: bool
    sped_up: bool
    confidence: float


def detect_speed(ratio: float, *, tolerance: float = 0.06) -> SpeedResult:
    if ratio <= 0:
        raise ValueError("speed ratio must be positive")
    confidence = min(1.0, abs(ratio - 1.0) / max(tolerance, 1e-9))
    slowed = ratio < 1.0 - tolerance
    sped_up = ratio > 1.0 + tolerance
    return SpeedResult(ratio, slowed, sped_up, confidence)
