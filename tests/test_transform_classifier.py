from musivex.transform_classifier import classify


def test_classifies_slowed_reverb() -> None:
    result = classify(tempo_ratio=0.8, envelope=[1, .9, .8, .7, .6, .5])
    assert result.slowed and result.reverb
