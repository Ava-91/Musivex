"""Helpers for selecting short fingerprint windows."""


def select_window(duration: float, *, max_seconds: float = 12.0) -> tuple[float, float]:
    """Return a representative start/length window for recognition."""
    if duration <= 0:
        raise ValueError("duration must be positive")
    length = min(duration, max_seconds)
    start = max(0.0, (duration - length) / 2.0)
    return start, length
