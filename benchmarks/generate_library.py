"""Generate empty deterministic files for filesystem benchmarks."""
from pathlib import Path

def generate_library(root: str | Path, count: int) -> Path:
    destination = Path(root)
    destination.mkdir(parents=True, exist_ok=True)
    for index in range(count):
        (destination / f"track-{index:05d}.mp3").touch()
    return destination
