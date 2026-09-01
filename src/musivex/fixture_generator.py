"""Generate tiny synthetic WAV fixtures for local evaluation."""

from pathlib import Path
import math
import wave


def write_tone(path: str | Path, *, frequency: float = 440.0, seconds: float = 0.25, rate: int = 8000) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    frames = bytearray()
    for index in range(int(seconds * rate)):
        sample = int(12000 * math.sin(2 * math.pi * frequency * index / rate))
        frames.extend(sample.to_bytes(2, "little", signed=True))
    with wave.open(str(target), "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(rate)
        audio.writeframes(frames)
    return target
