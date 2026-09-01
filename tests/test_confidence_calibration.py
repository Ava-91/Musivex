from musivex.confidence_calibration import calibrate, can_auto_apply
from musivex.review_decision import decide


def test_calibration_clamps() -> None:
    assert calibrate(2.0) == 1.0


def test_low_confidence_requires_review() -> None:
    result = decide(0.7, 0.85)
    assert result.requires_review
    assert not can_auto_apply(0.7, 0.85)
