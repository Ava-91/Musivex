"""Provider protocol for pluggable music recognition backends."""

from pathlib import Path
from typing import Protocol

from .recognition_models import RecognitionResult


class RecognitionProvider(Protocol):
    """Minimal contract implemented by every recognition backend."""

    name: str

    def identify(self, path: Path) -> RecognitionResult | None:
        """Identify one local audio file, returning None for no match."""
        ...
