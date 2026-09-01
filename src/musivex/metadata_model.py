"""Normalized metadata types."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class Artwork:
    data: bytes
    mime_type: str


@dataclass(frozen=True, slots=True)
class Transformation:
    slowed: bool = False
    sped_up: bool = False
    reverb: bool = False
    pitch_shift: float | None = None


@dataclass(slots=True)
class Metadata:
    title: str | None = None
    artist: str | None = None
    album: str | None = None
    album_artist: str | None = None
    release_date: str | None = None
    track_number: int | None = None
    disc_number: int | None = None
    genre: str | None = None
    recording_id: str | None = None
    release_id: str | None = None
    confidence: float | None = None
    artwork: Artwork | None = None
    transformation: Transformation = field(default_factory=Transformation)

    def as_dict(self) -> dict[str, Any]:
        result = {k: v for k, v in self.__dict__.items() if k != "artwork"}
        result["artwork"] = None if self.artwork is None else {"mime_type": self.artwork.mime_type}
        result["transformation"] = self.transformation.__dict__
        return result
