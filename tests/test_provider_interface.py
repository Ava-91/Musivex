from pathlib import Path

from musivex.recognition_models import RecognitionResult
from musivex.recognition_provider import RecognitionProvider
from musivex.recognition_registry import RecognitionRegistry


class ExampleProvider:
    name = "example"

    def identify(self, path: Path) -> RecognitionResult | None:
        return RecognitionResult("Example", "Artist", provider=self.name)


def test_registry_selects_provider() -> None:
    provider: RecognitionProvider = ExampleProvider()
    registry = RecognitionRegistry()
    registry.register(provider)
    assert registry.get("example").identify(Path("x.mp3")).title == "Example"
    assert registry.names() == ("example",)
