"""Backup restoration for metadata writes."""

from pathlib import Path
import shutil


def restore_backup(path: str | Path) -> Path:
    target = Path(path)
    backup = target.with_suffix(target.suffix + ".bak")
    if not backup.exists():
        raise FileNotFoundError(backup)
    shutil.copy2(backup, target)
    return target
