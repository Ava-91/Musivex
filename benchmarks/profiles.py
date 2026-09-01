"""Deterministic benchmark profiles."""
from dataclasses import dataclass

@dataclass(frozen=True)
class BenchmarkProfile:
    name: str
    file_count: int

PROFILES = (
    BenchmarkProfile("small", 100),
    BenchmarkProfile("medium", 1000),
    BenchmarkProfile("large", 10000),
)
