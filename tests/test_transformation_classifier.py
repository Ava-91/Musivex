from musivex.reverb_detector import ReverbResult
from musivex.speed_detector import SpeedResult
from musivex.transformation_classifier import classify
from musivex.transformation_labels import label


def test_slowed_reverb_combines() -> None:
    result = classify(SpeedResult(0.8, True, False, 0.9), ReverbResult(0.9, True, 0.8))
    assert label(result) == "Slowed + Reverb"
