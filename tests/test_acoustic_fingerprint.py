from pathlib import Path

import pytest

from musivex.acoustic_fingerprint import FingerprintError, generate_acoustic_fingerprint
from musivex.fingerprint_segments import select_window


def test_missing_audio_fails_cleanly(tmp_path: Path) -> None:
    with pytest.raises(FingerprintError):
        generate_acoustic_fingerprint(tmp_path / "missing.mp3")


def test_window_is_centered() -> None:
    assert select_window(100.0) == (44.0, 12.0)
