import pytest

from musivex.confidence import MatchDecision, assess


def test_confidence_bands() -> None:
    assert assess(0.95).decision == MatchDecision.AUTO
    assert assess(0.70).decision == MatchDecision.REVIEW
    assert assess(0.30).decision == MatchDecision.REJECT


def test_confidence_rejects_invalid_scores() -> None:
    with pytest.raises(ValueError):
        assess(2)
