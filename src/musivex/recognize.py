"""High-level recognition entry point."""

from pathlib import Path

from .recognition import Candidate, RecognitionProvider, rank_candidates


def recognize(path: str | Path, provider: RecognitionProvider) -> list[Candidate]:
    return rank_candidates(provider.identify(Path(path)))
