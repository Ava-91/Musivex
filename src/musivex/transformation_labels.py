"""Human-readable transformation labels."""

from .transformation_classifier import TransformationResult


def label(result: TransformationResult) -> str:
    parts: list[str] = []
    if result.slowed:
        parts.append("Slowed")
    if result.sped_up:
        parts.append("Sped Up")
    if result.reverb:
        parts.append("Reverb")
    return " + ".join(parts) if parts else "Original"
