"""Combine filename hints with measured tempo ratios."""

from .metadata_model import Transformation
from .tempo import classify_speed_ratio
from .transformations import detect_from_text


def detect(text: str, *, tempo_ratio: float | None = None) -> Transformation:
    result = detect_from_text(text)
    if tempo_ratio is None:
        return result
    speed = classify_speed_ratio(tempo_ratio)
    if speed == "slowed":
        return Transformation(slowed=True, reverb=result.reverb)
    if speed == "sped_up":
        return Transformation(sped_up=True, reverb=result.reverb)
    return result
