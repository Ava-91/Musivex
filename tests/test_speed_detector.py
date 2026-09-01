import pytest

from musivex.speed_detector import detect_speed


def test_detects_slowed() -> None:
    result = detect_speed(0.8)
    assert result.slowed is True
    assert result.sped_up is False


def test_normal_speed_is_neither() -> None:
    result = detect_speed(1.01)
    assert not result.slowed and not result.sped_up


def test_invalid_ratio() -> None:
    with pytest.raises(ValueError):
        detect_speed(0)
