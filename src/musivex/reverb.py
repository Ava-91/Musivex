"""Lightweight reverb feature heuristics."""

import math


def tail_decay_score(envelope: list[float]) -> float:
    """Estimate lingering energy from a normalized amplitude envelope."""
    if len(envelope) < 3:
        return 0.0
    values = [abs(float(value)) for value in envelope]
    peak = max(values)
    if peak == 0:
        return 0.0
    normalized = [value / peak for value in values]
    tail = normalized[len(normalized) // 2 :]
    lingering = sum(value for value in tail) / len(tail)
    return max(0.0, min(1.0, lingering * math.sqrt(len(tail))))


def has_reverb(envelope: list[float], threshold: float = 0.35) -> bool:
    return tail_decay_score(envelope) >= threshold
