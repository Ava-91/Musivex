"""In-memory review queue for uncertain matches."""

from dataclasses import dataclass, field

from .confidence import MatchAssessment, MatchDecision
from .recognition import Candidate


@dataclass
class ReviewQueue:
    items: list[tuple[Candidate, MatchAssessment]] = field(default_factory=list)

    def add(self, candidate: Candidate, assessment: MatchAssessment) -> None:
        if assessment.decision == MatchDecision.REVIEW:
            self.items.append((candidate, assessment))

    def pop(self) -> tuple[Candidate, MatchAssessment] | None:
        return self.items.pop(0) if self.items else None
