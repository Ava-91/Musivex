"""Preview metadata changes before committing them."""

from dataclasses import dataclass

from .metadata_model import Metadata


@dataclass(frozen=True, slots=True)
class WritePlan:
    path: str
    changes: dict[str, str]


def plan(path: str, metadata: Metadata) -> WritePlan:
    changes = {
        key: str(value)
        for key, value in {
            "title": metadata.title,
            "artist": metadata.artist,
            "album": metadata.album,
            "album_artist": metadata.album_artist,
            "release_date": metadata.release_date,
            "genre": metadata.genre,
        }.items()
        if value is not None
    }
    return WritePlan(path=path, changes=changes)
