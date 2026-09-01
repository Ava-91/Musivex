"""Download artwork with bounded size."""

from urllib.request import Request, urlopen


def fetch_artwork(url: str, *, max_bytes: int = 5_000_000) -> bytes:
    request = Request(url, headers={"User-Agent": "Musivex/0.1"})
    with urlopen(request, timeout=15) as response:
        data = response.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise ValueError("artwork exceeds configured size limit")
    return data
