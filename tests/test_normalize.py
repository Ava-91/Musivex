from musivex.normalize import normalize_result
from musivex.normalize_candidates import normalize_candidates


def test_normalizes_missing_fields_and_clamps_confidence() -> None:
    result = normalize_result({"title": " CHIHIRO ", "artist": "Billie Eilish", "confidence": 2}, provider="mock")
    assert result.title == "CHIHIRO"
    assert result.confidence == 1.0


def test_candidates_rank_highest_first() -> None:
    low = normalize_result({"title": "a", "confidence": 0.2}, provider="x")
    high = normalize_result({"title": "b", "confidence": 0.9}, provider="x")
    assert normalize_candidates([low, high])[0].title == "b"
