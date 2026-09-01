"""Conservative policy for conflicting transformation evidence."""

from .transformation_classifier import TransformationResult


def is_ambiguous(result: TransformationResult) -> bool:
    return result.slowed and result.sped_up
