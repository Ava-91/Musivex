"""Candidate matching and confidence utilities."""

from .recognition import Candidate, rank_candidates


def best_match(candidates: list[Candidate]) -> Candidate | None:
    ranked = rank_candidates(candidates)
    return ranked[0] if ranked else None


def confidence(candidates: list[Candidate]) -> float:
    best = best_match(candidates)
    return 0.0 if best is None else max(0.0, min(1.0, best.score))
