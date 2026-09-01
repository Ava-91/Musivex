"""Helpers for defensive parsing of remote provider responses."""


def result_or_none(payload: dict[str, object]) -> dict[str, object] | None:
    if payload.get("status") != "success":
        return None
    result = payload.get("result")
    return result if isinstance(result, dict) else None
