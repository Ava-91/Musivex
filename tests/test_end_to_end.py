from pathlib import Path

from musivex.end_to_end import run
from musivex.mock_provider import MockRecognitionProvider
from musivex.recognition_models import RecognitionResult
from musivex.pipeline_report import summary


def test_high_confidence_is_safe_to_apply(tmp_path: Path) -> None:
    result = run(MockRecognitionProvider(RecognitionResult("CHIHIRO", "Billie Eilish", confidence=0.99)), tmp_path / "x.mp3")
    assert result.should_write
    assert "CHIHIRO" in summary(result)


def test_low_confidence_requires_review(tmp_path: Path) -> None:
    result = run(MockRecognitionProvider(RecognitionResult("Unknown", "Artist", confidence=0.5)), tmp_path / "x.mp3")
    assert not result.should_write
