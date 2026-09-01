"""Read common metadata from audio containers using Mutagen."""

from pathlib import Path

from mutagen import File

from .metadata_model import Metadata


def read_metadata(path: str | Path) -> Metadata:
    audio = File(path, easy=True)
    if audio is None:
        raise ValueError(f"Unsupported or unreadable audio file: {path}")

    def first(key: str) -> str | None:
        value = audio.get(key)
        return value[0] if value else None

    return Metadata(
        title=first("title"),
        artist=first("artist"),
        album=first("album"),
        album_artist=first("albumartist"),
        release_date=first("date"),
        genre=first("genre"),
    )
