"""Tempo-ratio helpers for transformed audio candidates."""


def speed_ratio(original_tempo: float, candidate_tempo: float) -> float:
    if original_tempo <= 0 or candidate_tempo <= 0:
        raise ValueError("tempo values must be positive")
    return candidate_tempo / original_tempo


def classify_speed_ratio(ratio: float, tolerance: float = 0.06) -> str:
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    if ratio < 1 - tolerance:
        return "slowed"
    if ratio > 1 + tolerance:
        return "sped_up"
    return "original"
