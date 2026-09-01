"""Review and retry queues for uncertain batch results."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class ReviewQueue:
    pending: list[Path] = field(default_factory=list)
    failed: list[Path] = field(default_factory=list)

    def add_review(self, path: Path) -> None:
        if path not in self.pending:
            self.pending.append(path)

    def add_failed(self, path: Path) -> None:
        if path not in self.failed:
            self.failed.append(path)

    def retry_failed(self) -> list[Path]:
        retry = list(self.failed)
        self.failed.clear()
        return retry
