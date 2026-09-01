"""Small HTTP helpers kept separate for provider testing."""

from collections.abc import Callable

HttpPost = Callable[[str, bytes, dict[str, str], float], bytes]


def post_bytes(url: str, body: bytes, headers: dict[str, str], timeout: float) -> bytes:
    from urllib import request

    req = request.Request(url, data=body, method="POST", headers=headers)
    with request.urlopen(req, timeout=timeout) as response:
        return response.read()
