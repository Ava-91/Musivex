"""Small benchmark runner using Python's standard library."""
from time import perf_counter
from pathlib import Path

def benchmark_scan(root: str | Path) -> dict[str, float | int]:
    start = perf_counter()
    files = list(Path(root).rglob("*.mp3"))
    elapsed = perf_counter() - start
    return {"files": len(files), "seconds": elapsed, "files_per_second": len(files) / elapsed if elapsed else float("inf")}
