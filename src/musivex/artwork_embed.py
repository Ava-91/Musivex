"""Container-aware artwork embedding helpers."""

from pathlib import Path

from mutagen import File
from mutagen.flac import Picture
from mutagen.id3 import APIC, ID3
from mutagen.mp4 import MP4, MP4Cover

from .artwork_validation import ArtworkPayload


def embed_artwork(path: str | Path, artwork: ArtworkPayload, *, replace: bool = False) -> None:
    target = Path(path)
    suffix = target.suffix.lower()
    if suffix == ".mp3":
        tags = ID3(target)
        if not replace and tags.getall("APIC:"):
            return
        if replace:
            tags.delall("APIC:")
        tags.add(APIC(mime=artwork.mime_type, type=3, desc="Cover", data=artwork.data))
        tags.save(target)
        return
    if suffix == ".flac":
        audio = File(target)
        if audio is None:
            raise ValueError(f"unsupported audio file: {target}")
        if not replace and audio.pictures:
            return
        if replace:
            audio.clear_pictures()
        picture = Picture(artwork.data)
        picture.type = 3
        picture.mime = artwork.mime_type
        audio.add_picture(picture)
        audio.save()
        return
    if suffix in {".m4a", ".mp4"}:
        audio = MP4(target)
        if not replace and audio.tags and audio.tags.get("covr"):
            return
        image_format = MP4Cover.FORMAT_PNG if artwork.mime_type == "image/png" else MP4Cover.FORMAT_JPEG
        audio["covr"] = [MP4Cover(artwork.data, imageformat=image_format)]
        audio.save()
        return
    raise ValueError(f"artwork embedding is unsupported for {suffix or 'unknown'}")
