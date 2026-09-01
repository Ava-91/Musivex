"""Human-readable explanations for transformation detections."""

from .metadata_model import Transformation


def describe(value: Transformation) -> str:
    parts: list[str] = []
    if value.slowed:
        parts.append("slowed")
    if value.sped_up:
        parts.append("sped up")
    if value.reverb:
        parts.append("reverb")
    if value.pitch_shift is not None:
        parts.append(f"pitch shift {value.pitch_shift:+.2f} semitones")
    return " + ".join(parts) if parts else "original"
