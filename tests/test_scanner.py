from pathlib import Path

from musivex.scanner import scan


def test_scan_recursively_finds_supported_files(tmp_path: Path) -> None:
    (tmp_path / "b.mp3").touch()
    nested = tmp_path / "nested"
    nested.mkdir()
    (nested / "a.FLAC").touch()
    (tmp_path / "notes.txt").touch()

    result = scan(tmp_path)

    assert [item.path.name for item in result] == ["b.mp3", "a.FLAC"]
    assert [item.extension for item in result] == ["mp3", "flac"]


def test_scan_single_unsupported_file_returns_empty(tmp_path: Path) -> None:
    file = tmp_path / "notes.txt"
    file.touch()
    assert scan(file) == []
