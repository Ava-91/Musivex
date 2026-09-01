"""Pitch-preserving transformation helpers."""


def classify_pitch_change(reference_hz: float, candidate_hz: float, *, tolerance: float = 0.03) -> float:
    if reference_hz <= 0 or candidate_hz <= 0:
        raise ValueError("frequencies must be positive")
    return candidate_hz / reference_hz if abs(candidate_hz - reference_hz) > reference_hz * tolerance else 1.0
