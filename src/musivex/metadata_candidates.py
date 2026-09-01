"""Choose the best metadata candidate conservatively."""

from .metadata_model import Metadata


def choose_candidate(candidates: list[Metadata]) -> Metadata | None:
    if not candidates:
        return None
    return candidates[0]
