"""Validation helpers for normalized metadata."""

from .metadata_model import Metadata


def validate(metadata: Metadata) -> list[str]:
    errors: list[str] = []
    if metadata.confidence is not None and not 0 <= metadata.confidence <= 1:
        errors.append("confidence must be between 0 and 1")
    if metadata.track_number is not None and metadata.track_number < 1:
        errors.append("track_number must be positive")
    if metadata.disc_number is not None and metadata.disc_number < 1:
        errors.append("disc_number must be positive")
    return errors
