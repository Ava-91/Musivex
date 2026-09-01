from pathlib import Path

from musivex.batch_processing import process_batch
from musivex.batch_report import BatchSummary
from musivex.batch_review import ReviewQueue
from musivex.progress import Progress, status_counts


def test_batch_isolates_failures(tmp_path: Path) -> None:
    good = tmp_path / "good.mp3"
    bad = tmp_path / "bad.mp3"
    good.write_bytes(b"x")
    bad.write_bytes(b"x")

    def operation(path: Path) -> str:
        if path.name == "bad.mp3":
            raise ValueError("broken")
        return "ok"

    results = process_batch([good, bad], operation)
    assert [result.status for result in results] == ["success", "failed"]
    assert results[1].error == "broken"


def test_progress_and_status_counts() -> None:
    assert Progress(4, 2).percent == 50
    assert status_counts(["success", "review", "failed"]) == {
        "success": 1, "review": 1, "skipped": 0, "failed": 1
    }


def test_review_queue_retries_failures(tmp_path: Path) -> None:
    path = tmp_path / "song.mp3"
    queue = ReviewQueue()
    queue.add_failed(path)
    assert queue.retry_failed() == [path]
    assert queue.failed == []


def test_summary_has_json_and_text() -> None:
    summary = BatchSummary(success=2, review=1, failed=1)
    assert '"success": 2' in summary.to_json()
    assert "review: 1" in summary.to_text()
