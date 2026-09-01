"""Embedded artwork extraction helpers."""

from pathlib import Path

from mutagen import File

from .metadata_model import Artwork


def read_artwork(path: str | Path) -> Artwork | None:
    audio = File(path)
    if audio is None:
        return None
    pictures = getattr(audio, "pictures", None)
    if pictures:
        picture = pictures[0]
        return Artwork(data=picture.data, mime_type=picture.mime)
    return None
