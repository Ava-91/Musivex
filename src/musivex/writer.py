"""Safe metadata writing."""

from pathlib import Path
import shutil

from mutagen import File

from .metadata_model import Metadata

_FIELD_MAP = {
    "title": "title", "artist": "artist", "album": "album",
    "album_artist": "albumartist", "release_date": "date", "genre": "genre",
}


def write_metadata(path: str | Path, metadata: Metadata, *, dry_run: bool = True, backup: bool = True) -> None:
    target = Path(path)
    audio = File(target, easy=True)
    if audio is None:
        raise ValueError(f"Unsupported or unreadable audio file: {target}")
    if dry_run:
        return
    if backup:
        shutil.copy2(target, target.with_suffix(target.suffix + ".bak"))
    for source, destination in _FIELD_MAP.items():
        value = getattr(metadata, source)
        if value is not None:
            audio[destination] = [str(value)]
    audio.save()
