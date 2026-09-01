from musivex.reverb import has_reverb, tail_decay_score


def test_short_envelope_has_no_reverb_evidence() -> None:
    assert tail_decay_score([1.0, 0.0]) == 0.0


def test_lingering_tail_can_cross_threshold() -> None:
    envelope = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
    assert has_reverb(envelope)
