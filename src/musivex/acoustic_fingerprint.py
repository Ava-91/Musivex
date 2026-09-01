"""Acoustic fingerprint adapter using Chromaprint's fpcalc executable."""

from dataclasses import dataclass
from pathlib import Path
import json
import subprocess


class FingerprintError(RuntimeError):
    """Raised when an acoustic fingerprint cannot be produced."""


@dataclass(frozen=True, slots=True)
class AcousticFingerprint:
    fingerprint: str
    duration: float


def generate_acoustic_fingerprint(path: str | Path) -> AcousticFingerprint:
    source = Path(path)
    if not source.is_file():
        raise FingerprintError(f"audio file does not exist: {source}")
    try:
        completed = subprocess.run(
            ["fpcalc", "-json", str(source)],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        fingerprint = payload.get("fingerprint")
        duration = payload.get("duration")
        if not fingerprint or not isinstance(duration, (int, float)):
            raise FingerprintError("fpcalc returned an incomplete fingerprint")
        return AcousticFingerprint(str(fingerprint), float(duration))
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        raise FingerprintError("Chromaprint/fpcalc could not fingerprint the file") from exc
