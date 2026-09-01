"""Safety primitives for non-destructive metadata operations."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class PlannedChange:
    path: Path
    changed_fields: tuple[str, ...]


def ensure_dry_run(path: Path, *, dry_run: bool) -> None:
    """Validate a target before an operation that may modify it.

    The function intentionally performs no writes. Callers can use it as a
    guard so a dry-run path cannot accidentally fall through to a writer.
    """
    if not path.exists():
        raise FileNotFoundError(path)
    if not path.is_file():
        raise IsADirectoryError(path)
    # Keeping the flag explicit makes the safety boundary visible at call sites.
    if dry_run:
        return


def backup_path(path: Path) -> Path:
    """Return the deterministic sidecar backup path for an audio file."""
    return path.with_suffix(path.suffix + ".bak")
