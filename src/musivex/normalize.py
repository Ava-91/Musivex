"""Provider-independent recognition result normalization."""

from collections.abc import Mapping

from .recognition_models import RecognitionResult


def normalize_result(payload: Mapping[str, object], *, provider: str) -> RecognitionResult:
    def text(key: str) -> str | None:
        value = payload.get(key)
        return value.strip() if isinstance(value, str) and value.strip() else None

    raw_confidence = payload.get("confidence", 0.0)
    confidence = float(raw_confidence) if isinstance(raw_confidence, (int, float)) else 0.0
    return RecognitionResult(
        title=text("title"), artist=text("artist"), album=text("album"),
        recording_id=text("recording_id"), release_id=text("release_id"),
        confidence=max(0.0, min(1.0, confidence)), provider=provider,
        raw=dict(payload),
    )
