from pathlib import Path

import pytest

from musivex.audd_provider import AudDProvider
from musivex.recognition_errors import RecognitionConfigurationError


def test_audd_requires_token(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("AUDD_API_TOKEN", raising=False)
    with pytest.raises(RecognitionConfigurationError):
        AudDProvider()


def test_audd_name() -> None:
    monkeypatch_token = AudDProvider("test")
    assert monkeypatch_token.name == "audd"
