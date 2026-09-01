import pytest

from musivex.reverb_detector import detect_reverb
from musivex.reverb_features import decay_ratio


def test_detects_high_decay_score() -> None:
    result = detect_reverb(0.8)
    assert result.detected


def test_low_decay_is_not_reverb() -> None:
    assert not detect_reverb(0.2).detected


def test_decay_ratio() -> None:
    assert decay_ratio(10, 5) == pytest.approx(0.5)
