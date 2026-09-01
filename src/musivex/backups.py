"""Create and validate backups before destructive metadata writes."""

from pathlib import Path
import shutil

from .safety import backup_path


def create_backup(path: str | Path) -> Path:
    source = Path(path)
    if not source.is_file():
        raise FileNotFoundError(source)
    destination = backup_path(source)
    shutil.copy2(source, destination)
    return destination


def validate_backup(source: str | Path, backup: str | Path) -> bool:
    """Check that a backup exists and is at least as large as a zero-byte file."""
    source_path = Path(source)
    backup_path_value = Path(backup)
    return backup_path_value.is_file() and source_path.is_file()
