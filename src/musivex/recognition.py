"""Recognition provider interfaces and result types."""

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from .metadata_model import Metadata


@dataclass(frozen=True, slots=True)
class Candidate:
    metadata: Metadata
    score: float


class RecognitionProvider(Protocol):
    def identify(self, path: Path) -> list[Candidate]: ...


def rank_candidates(candidates: list[Candidate]) -> list[Candidate]:
    return sorted(candidates, key=lambda candidate: candidate.score, reverse=True)
