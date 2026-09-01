"""Candidate normalization helpers."""

from .recognition_models import RecognitionResult


def normalize_candidates(items: list[RecognitionResult]) -> list[RecognitionResult]:
    return sorted(items, key=lambda item: item.confidence, reverse=True)
