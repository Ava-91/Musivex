"""Explain recognition candidates without writing metadata."""

from .confidence import MatchAssessment, assess
from .recognition import Candidate


def assess_candidate(candidate: Candidate, *, auto_threshold: float = 0.90) -> MatchAssessment:
    return assess(candidate.score, auto_threshold=auto_threshold)
