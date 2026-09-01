from pathlib import Path

from musivex.mock_provider import MockRecognitionProvider
from musivex.recognition_models import RecognitionResult
from musivex.recognition_pipeline import recognize_file


def test_mock_provider_is_deterministic(tmp_path: Path) -> None:
    result = RecognitionResult("CHIHIRO", "Billie Eilish", confidence=0.99, provider="mock")
    provider = MockRecognitionProvider(result)
    assert recognize_file(provider, tmp_path / "song.mp3") == result
