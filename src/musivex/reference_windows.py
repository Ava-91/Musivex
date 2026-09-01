"""Window helpers for robust reference comparisons."""


def windows(length: int, *, size: int = 128, step: int = 64) -> list[tuple[int, int]]:
    if length <= 0:
        return []
    return [(start, min(start + size, length)) for start in range(0, length, step)]
