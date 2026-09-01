from musivex.transformation_pipeline import detect


def test_combined_signal_keeps_reverb() -> None:
    result = detect("unknown version (reverb)", tempo_ratio=0.8)
    assert result.slowed and result.reverb
