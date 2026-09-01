"""Simple benchmark regression thresholds."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Thresholds:
    max_scan_seconds: float = 10.0
    min_files_per_second: float = 100.0

def check_scan(result: dict[str, float | int], thresholds: Thresholds = Thresholds()) -> list[str]:
    failures: list[str] = []
    if float(result.get("seconds", 0)) > thresholds.max_scan_seconds:
        failures.append("scan time exceeded threshold")
    if float(result.get("files_per_second", 0)) < thresholds.min_files_per_second:
        failures.append("scan throughput fell below threshold")
    return failures
