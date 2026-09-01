import pytest

from musivex.tempo import classify_speed_ratio, speed_ratio
from musivex.transformations import detect_from_text


def test_detect_slowed_reverb() -> None:
    result = detect_from_text("Song (Slowed + Reverb)")
    assert result.slowed and result.reverb and not result.sped_up


def test_speed_ratio_classification() -> None:
    assert speed_ratio(120, 90) == 0.75
    assert classify_speed_ratio(0.75) == "slowed"
    assert classify_speed_ratio(1.0) == "original"
    assert classify_speed_ratio(1.25) == "sped_up"
    with pytest.raises(ValueError):
        speed_ratio(0, 100)
