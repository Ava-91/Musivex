"""Reference-track comparison primitives."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True, slots=True)
class ComparisonResult:
    time_ratio: float
    spectral_similarity: float
    confidence: float


def compare_features(reference: list[float], candidate: list[float]) -> ComparisonResult:
    if not reference or not candidate:
        raise ValueError("both feature sequences are required")
    ratio = len(candidate) / len(reference)
    n = min(len(reference), len(candidate))
    distance = sum(abs(reference[i] - candidate[i]) for i in range(n)) / n
    similarity = max(0.0, 1.0 - distance)
    confidence = similarity if isfinite(similarity) else 0.0
    return ComparisonResult(ratio, confidence, confidence)
