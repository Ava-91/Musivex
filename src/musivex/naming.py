"""Canonical naming for transformed tracks."""

import re

from .metadata_model import Transformation

_SUFFIXES = re.compile(r"\s*\((?:slowed|sped up|reverb|pitch shift).*\)$", re.I)


def variant_title(title: str, transformation: Transformation, template: str = "{title} ({variant})") -> str:
    base = _SUFFIXES.sub("", title).strip()
    parts: list[str] = []
    if transformation.slowed:
        parts.append("Slowed")
    if transformation.sped_up:
        parts.append("Sped Up")
    if transformation.reverb:
        parts.append("Reverb")
    if transformation.pitch_shift is not None:
        parts.append(f"Pitch {transformation.pitch_shift:+.1f} semitones")
    return base if not parts else template.format(title=base, variant=" + ".join(parts))
