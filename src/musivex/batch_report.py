"""Human- and machine-readable batch summaries."""

from dataclasses import dataclass
import json


@dataclass(frozen=True, slots=True)
class BatchSummary:
    success: int = 0
    review: int = 0
    skipped: int = 0
    failed: int = 0

    def as_dict(self) -> dict[str, int]:
        return {
            "success": self.success,
            "review": self.review,
            "skipped": self.skipped,
            "failed": self.failed,
        }

    def to_json(self) -> str:
        return json.dumps(self.as_dict(), sort_keys=True)

    def to_text(self) -> str:
        return " | ".join(f"{key}: {value}" for key, value in self.as_dict().items())
