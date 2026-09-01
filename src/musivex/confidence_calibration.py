"""Confidence thresholds and calibration helpers."""


def calibrate(raw: float, *, slope: float = 1.0, intercept: float = 0.0) -> float:
    value = slope * raw + intercept
    return max(0.0, min(1.0, value))


def can_auto_apply(confidence: float, threshold: float) -> bool:
    return confidence >= threshold
