"""Combine reverb and speed evidence into a transformation result."""

from .metadata_model import Transformation
from .reverb import has_reverb
from .tempo import classify_speed_ratio


def classify(*, tempo_ratio: float | None = None, envelope: list[float] | None = None) -> Transformation:
    slowed = sped_up = False
    if tempo_ratio is not None:
        speed = classify_speed_ratio(tempo_ratio)
        slowed, sped_up = speed == "slowed", speed == "sped_up"
    reverb = envelope is not None and has_reverb(envelope)
    return Transformation(slowed=slowed, sped_up=sped_up, reverb=reverb)
