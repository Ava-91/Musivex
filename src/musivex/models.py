"""Core models shared by Musivex components."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class AudioFile:
    path: Path
    extension: str

    @classmethod
    def from_path(cls, path: Path) -> "AudioFile":
        return cls(path=path, extension=path.suffix.lower().lstrip("."))
