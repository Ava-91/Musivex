"""Conservative speed transformation thresholds."""

DEFAULT_SPEED_TOLERANCE = 0.06


def is_near_normal(ratio: float, tolerance: float = DEFAULT_SPEED_TOLERANCE) -> bool:
    return abs(ratio - 1.0) <= tolerance
