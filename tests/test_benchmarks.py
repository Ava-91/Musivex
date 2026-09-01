from pathlib import Path

from benchmarks.generate_library import generate_library
from benchmarks.runner import benchmark_scan
from benchmarks.thresholds import Thresholds, check_scan


def test_benchmarks_package_is_importable() -> None:
    import benchmarks

    assert benchmarks.__doc__ == "Benchmark helpers for Musivex."


def test_generated_profile_is_deterministic(tmp_path: Path) -> None:
    root = generate_library(tmp_path / "library", 5)
    result = benchmark_scan(root)
    assert result["files"] == 5


def test_regression_thresholds_report_failures() -> None:
    failures = check_scan(
        {"seconds": 2.0, "files_per_second": 10},
        Thresholds(max_scan_seconds=1, min_files_per_second=100),
    )
    assert len(failures) == 2
