import pytest

from musivex.evaluation import classification_metrics
from musivex.fixture_generator import write_tone


def test_metrics_report_accuracy_and_errors() -> None:
    metrics = classification_metrics([True, True, False, False], [True, False, True, False])
    assert metrics.accuracy == 0.5
    assert metrics.false_positives == 1
    assert metrics.false_negatives == 1


def test_metrics_require_equal_lengths() -> None:
    with pytest.raises(ValueError):
        classification_metrics([True], [])


def test_synthetic_fixture_generator(tmp_path) -> None:
    path = write_tone(tmp_path / "fixture.wav", frequency=220)
    assert path.exists()
    assert path.stat().st_size > 44
