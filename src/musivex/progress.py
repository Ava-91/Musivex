"""Progress and per-file status tracking."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Progress:
    total: int
    completed: int = 0

    @property
    def percent(self) -> float:
        return 100.0 if self.total == 0 else self.completed / self.total * 100


def status_counts(statuses: list[str]) -> dict[str, int]:
    counts = {"success": 0, "review": 0, "skipped": 0, "failed": 0}
    for status in statuses:
        counts[status] = counts.get(status, 0) + 1
    return counts
