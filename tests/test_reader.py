from pathlib import Path

import pytest

from musivex.reader import read_metadata


def test_reader_rejects_unknown_container(tmp_path: Path) -> None:
    path = tmp_path / "not-audio.bin"
    path.write_bytes(b"not audio")
    with pytest.raises(ValueError):
        read_metadata(path)
