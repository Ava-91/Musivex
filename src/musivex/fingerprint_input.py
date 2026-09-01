"""Validation helpers for fingerprint inputs."""

from pathlib import Path

SUPPORTED_AUDIO_SUFFIXES = {".mp3", ".flac", ".m4a", ".wav", ".ogg", ".opus", ".aac"}


def validate_fingerprint_input(path: str | Path) -> Path:
    source = Path(path)
    if not source.is_file():
        raise ValueError(f"not a file: {source}")
    if source.suffix.lower() not in SUPPORTED_AUDIO_SUFFIXES:
        raise ValueError(f"unsupported audio format: {source.suffix or '<none>'}")
    return source
