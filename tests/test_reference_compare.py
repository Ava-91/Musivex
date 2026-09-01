import pytest

from musivex.reference_compare import compare_features
from musivex.reference_windows import windows


def test_comparison_is_identical_for_identical_features() -> None:
    result = compare_features([0.1, 0.2], [0.1, 0.2])
    assert result.spectral_similarity == pytest.approx(1.0)
    assert result.time_ratio == pytest.approx(1.0)


def test_windows_are_bounded() -> None:
    assert windows(200, size=100, step=100) == [(0, 100), (100, 200)]
