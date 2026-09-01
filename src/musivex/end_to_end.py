"""Safe end-to-end recognition orchestration."""

from dataclasses import dataclass
from pathlib import Path

from .confidence_calibration import can_auto_apply
from .recognition_models import RecognitionResult
from .recognition_pipeline import recognize_file
from .recognition_provider import RecognitionProvider


@dataclass(frozen=True, slots=True)
class PipelineResult:
    recognition: RecognitionResult | None
    should_write: bool


def run(provider: RecognitionProvider, path: str | Path, *, threshold: float = 0.85) -> PipelineResult:
    result = recognize_file(provider, path)
    return PipelineResult(result, bool(result and can_auto_apply(result.confidence, threshold)))
