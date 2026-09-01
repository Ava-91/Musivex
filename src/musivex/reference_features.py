"""Provider-neutral scalar feature extraction for comparisons."""


def normalize(values: list[float]) -> list[float]:
    if not values:
        return []
    peak = max(abs(value) for value in values) or 1.0
    return [value / peak for value in values]
