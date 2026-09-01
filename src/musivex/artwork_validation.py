"""Validation for downloaded and embedded cover artwork."""

from dataclasses import dataclass


ALLOWED_MIME_TYPES = frozenset({"image/jpeg", "image/png"})


@dataclass(frozen=True, slots=True)
class ArtworkPayload:
    data: bytes
    mime_type: str


def validate_artwork(data: bytes, mime_type: str, *, max_bytes: int = 10_000_000) -> ArtworkPayload:
    if not data:
        raise ValueError("artwork is empty")
    if mime_type not in ALLOWED_MIME_TYPES:
        raise ValueError(f"unsupported artwork type: {mime_type}")
    if len(data) > max_bytes:
        raise ValueError("artwork exceeds configured size limit")
    return ArtworkPayload(data=data, mime_type=mime_type)
