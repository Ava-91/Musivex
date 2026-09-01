"""Small registry for selecting recognition providers."""

from .recognition_provider import RecognitionProvider


class RecognitionRegistry:
    def __init__(self) -> None:
        self._providers: dict[str, RecognitionProvider] = {}

    def register(self, provider: RecognitionProvider) -> None:
        self._providers[provider.name] = provider

    def get(self, name: str) -> RecognitionProvider:
        return self._providers[name]

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._providers))
