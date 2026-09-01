import logging
from pathlib import Path

from musivex.diagnostic_format import format_diagnostic
from musivex.diagnostics import Diagnostic, diagnostic_from_exception
from musivex.logging import EventFormatter, get_logger
from musivex.timing import timed


def test_diagnostic_contains_stage_and_path(tmp_path: Path) -> None:
    diagnostic = diagnostic_from_exception(tmp_path / "song.mp3", "recognition", ValueError("no match"), "musicbrainz")
    assert diagnostic.stage == "recognition"
    assert diagnostic.provider == "musicbrainz"
    assert "no match" in format_diagnostic(diagnostic)


def test_event_formatter_emits_json() -> None:
    record = logging.LogRecord("test", logging.INFO, "", 0, "started", (), None)
    record.event = "scan.started"
    output = EventFormatter().format(record)
    assert '"event": "scan.started"' in output


def test_logger_is_reusable() -> None:
    logger = get_logger("musivex-test")
    assert get_logger("musivex-test") is logger


def test_timed_reports_elapsed_time() -> None:
    captured = []
    with timed("scan", lambda stage, seconds: captured.append((stage, seconds))):
        pass
    assert captured[0][0] == "scan"
    assert captured[0][1] >= 0
