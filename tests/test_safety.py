from pathlib import Path

import pytest

from musivex.atomic_write import atomic_replace
from musivex.backups import create_backup
from musivex.rollback_state import BackupRecord, load_record, save_record
from musivex.safety import backup_path, ensure_dry_run


def test_dry_run_guard_does_not_write(tmp_path: Path) -> None:
    target = tmp_path / "song.mp3"
    target.write_bytes(b"original")
    ensure_dry_run(target, dry_run=True)
    assert target.read_bytes() == b"original"


def test_backup_is_deterministic(tmp_path: Path) -> None:
    target = tmp_path / "song.mp3"
    target.write_bytes(b"audio")
    backup = create_backup(target)
    assert backup == backup_path(target)
    assert backup.read_bytes() == b"audio"


def test_atomic_replace_updates_target(tmp_path: Path) -> None:
    target = tmp_path / "song.mp3"
    source = tmp_path / "new.mp3"
    target.write_bytes(b"old")
    source.write_bytes(b"new")
    atomic_replace(source, target)
    assert target.read_bytes() == b"new"


def test_rollback_record_round_trip(tmp_path: Path) -> None:
    journal = tmp_path / "rollback.json"
    record = BackupRecord("song.mp3", "song.mp3.bak")
    save_record(record, journal)
    assert load_record(journal) == record


def test_missing_target_is_rejected(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        ensure_dry_run(tmp_path / "missing.mp3", dry_run=True)
