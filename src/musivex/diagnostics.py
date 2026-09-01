"""Actionable diagnostics for per-file and provider failures."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Diagnostic:
    path: Path | None
    stage: str
    message: str
    provider: str | None = None

    def as_dict(self) -> dict[str, str | None]:
        return {
            "path": str(self.path) if self.path else None,
            "stage": self.stage,
            "message": self.message,
            "provider": self.provider,
        }


def diagnostic_from_exception(path: Path | None, stage: str, exc: Exception, provider: str | None = None) -> Diagnostic:
    return Diagnostic(path=path, stage=stage, message=str(exc) or exc.__class__.__name__, provider=provider)
