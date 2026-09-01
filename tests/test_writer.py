from pathlib import Path

from musivex.metadata_model import Metadata
from musivex.writer import write_metadata


def test_dry_run_never_creates_backup(tmp_path: Path) -> None:
    path = tmp_path / "track.mp3"
    path.write_bytes(b"not a real mp3")
    try:
        write_metadata(path, Metadata(title="Example"), dry_run=True)
    except ValueError:
        pass
    assert not path.with_suffix(".mp3.bak").exists()
