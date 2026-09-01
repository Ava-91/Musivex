"""Detection and representation of common track transformations."""

import re

from .metadata_model import Transformation

_SLOWED = re.compile(r"\b(slow(?:ed|er)?|nightcore[- ]?slow(?:ed)?)\b", re.I)
_SPEED = re.compile(r"\b(speed(?:ed)?[- ]?up|faster)\b", re.I)
_REVERB = re.compile(r"\b(reverb|echo(?:ed)?)\b", re.I)


def detect_from_text(text: str) -> Transformation:
    return Transformation(
        slowed=bool(_SLOWED.search(text)),
        sped_up=bool(_SPEED.search(text)),
        reverb=bool(_REVERB.search(text)),
    )
