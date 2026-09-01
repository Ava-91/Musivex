"""Provider-agnostic recognition pipeline entry point."""

from pathlib import Path

from .recognition_models import RecognitionResult
from .recognition_provider import RecognitionProvider


def recognize_file(provider: RecognitionProvider, path: str | Path) -> RecognitionResult | None:
    return provider.identify(Path(path))
