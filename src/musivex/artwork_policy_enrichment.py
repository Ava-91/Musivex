"""Policy for preserving existing artwork."""


def should_replace(existing: bool, *, force: bool = False) -> bool:
    return force or not existing
