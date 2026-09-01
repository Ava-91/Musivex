"""Normalized models shared by recognition providers."""

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class RecognitionResult:
    title: str | None
    artist: str | None
    album: str | None = None
    recording_id: str | None = None
    release_id: str | None = None
    confidence: float = 0.0
    provider: str = "unknown"
    raw: dict[str, object] = field(default_factory=dict)
