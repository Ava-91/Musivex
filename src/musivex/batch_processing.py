"""Failure-isolated batch processing primitives."""

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class BatchResult:
    path: Path
    status: str
    value: T | None = None
    error: str | None = None


def process_batch(paths: list[Path], operation: Callable[[Path], T]) -> list[BatchResult]:
    """Run an operation for every path without aborting on one failure."""
    results: list[BatchResult] = []
    for path in paths:
        try:
            results.append(BatchResult(path, "success", operation(path)))
        except Exception as exc:  # noqa: BLE001 - batch isolation is intentional.
            results.append(BatchResult(path, "failed", error=str(exc)))
    return results
