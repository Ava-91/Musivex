"""Deterministic recognition provider for tests and demos."""

from pathlib import Path

from .recognition_models import RecognitionResult


class MockRecognitionProvider:
    name = "mock"

    def __init__(self, result: RecognitionResult | None = None) -> None:
        self.result = result

    def identify(self, path: Path) -> RecognitionResult | None:
        return self.result
