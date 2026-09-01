"""Combine independent transformation signals."""

from dataclasses import dataclass

from .reverb_detector import ReverbResult
from .speed_detector import SpeedResult


@dataclass(frozen=True, slots=True)
class TransformationResult:
    slowed: bool
    sped_up: bool
    reverb: bool
    confidence: float


def classify(speed: SpeedResult, reverb: ReverbResult) -> TransformationResult:
    confidence = (speed.confidence + reverb.confidence) / 2.0
    return TransformationResult(speed.slowed, speed.sped_up, reverb.detected, min(1.0, confidence))
