"""AudD-backed online music recognition provider."""

import json
import os
from pathlib import Path
from urllib import request

from .recognition_errors import RecognitionConfigurationError, RecognitionTransportError
from .recognition_models import RecognitionResult


class AudDProvider:
    name = "audd"
    endpoint = "https://api.audd.io/"
    max_bytes = 10 * 1024 * 1024

    def __init__(self, api_token: str | None = None, *, timeout: float = 30.0) -> None:
        self.api_token = api_token or os.getenv("AUDD_API_TOKEN")
        self.timeout = timeout
        if not self.api_token:
            raise RecognitionConfigurationError("set AUDD_API_TOKEN before using AudDProvider")

    def identify(self, path: Path) -> RecognitionResult | None:
        source = Path(path)
        if not source.is_file():
            raise RecognitionTransportError(f"audio file does not exist: {source}")
        if source.stat().st_size > self.max_bytes:
            raise RecognitionTransportError("AudD standard recognition accepts files up to 10 MB")
        body = _multipart(self.api_token, source)
        req = request.Request(self.endpoint, data=body, method="POST", headers={"Content-Type": _CONTENT_TYPE})
        try:
            with request.urlopen(req, timeout=self.timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except Exception as exc:
            raise RecognitionTransportError("AudD request failed") from exc
        if payload.get("status") != "success":
            raise RecognitionTransportError(str(payload.get("error") or "AudD returned an error"))
        result = payload.get("result")
        if not result:
            return None
        return RecognitionResult(
            title=result.get("title"),
            artist=result.get("artist"),
            album=result.get("album"),
            confidence=1.0,
            provider=self.name,
            raw=result,
        )


_BOUNDARY = "----MusivexBoundary7f3a"
_CONTENT_TYPE = f"multipart/form-data; boundary={_BOUNDARY}"


def _multipart(token: str, source: Path) -> bytes:
    data = source.read_bytes()
    parts = [
        f"--{_BOUNDARY}\r\nContent-Disposition: form-data; name=\"api_token\"\r\n\r\n{token}\r\n".encode(),
        f"--{_BOUNDARY}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{source.name}\"\r\nContent-Type: application/octet-stream\r\n\r\n".encode() + data + b"\r\n",
        f"--{_BOUNDARY}--\r\n".encode(),
    ]
    return b"".join(parts)
