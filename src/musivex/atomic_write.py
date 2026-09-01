"""Atomic filesystem replacement helpers."""

from pathlib import Path
import os
import shutil
import tempfile


def atomic_replace(source: str | Path, target: str | Path) -> Path:
    """Copy *source* to a temporary sibling and atomically replace *target*."""
    source_path = Path(source)
    target_path = Path(target)
    if not source_path.is_file():
        raise FileNotFoundError(source_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    fd, temporary_name = tempfile.mkstemp(
        prefix=f".{target_path.name}.", suffix=".tmp", dir=target_path.parent
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(fd, "wb") as handle, source_path.open("rb") as source_handle:
            shutil.copyfileobj(source_handle, handle)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, target_path)
    finally:
        temporary_path.unlink(missing_ok=True)
    return target_path
