from pathlib import Path

from musivex.mock_provider import MockRecognitionProvider
from musivex.recognition_models import RecognitionResult
from musivex.recognition_pipeline import recognize_file


def test_mock_provider_can_model_no_match(tmp_path: Path) -> None:
    assert recognize_file(MockRecognitionProvider(None), tmp_path / "unknown.mp3") is None


def test_mock_provider_preserves_provider_name(tmp_path: Path) -> None:
    result = RecognitionResult("Song", "Artist", provider="mock")
    assert recognize_file(MockRecognitionProvider(result), tmp_path / "x.mp3").provider == "mock"
