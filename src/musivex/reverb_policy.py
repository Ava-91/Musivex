"""False-positive guards for reverb detection."""


def should_compare_against_reference(similarity: float) -> bool:
    return 0.0 <= similarity <= 1.0 and similarity >= 0.5
