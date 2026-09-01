"""Audio library scanning utilities."""

from pathlib import Path

SUPPORTED_EXTENSIONS = frozenset({".mp3", ".flac", ".m4a", ".mp4", ".wav"})


def scan(path: str | Path, *, recursive: bool = True) -> list[Path]:
    root = Path(path).expanduser()
    if not root.exists():
        raise FileNotFoundError(root)
    if root.is_file():
        return [root] if root.suffix.lower() in SUPPORTED_EXTENSIONS else []
    iterator = root.rglob("*") if recursive else root.glob("*")
    return sorted(
        (item for item in iterator if item.is_file() and item.suffix.lower() in SUPPORTED_EXTENSIONS),
        key=lambda item: item.as_posix().casefold(),
    )
