from pathlib import Path

from musivex.artwork import read_artwork


def test_read_artwork_returns_none_for_unknown_file(tmp_path: Path) -> None:
    path = tmp_path / "empty.bin"
    path.write_bytes(b"x")
    assert read_artwork(path) is None
