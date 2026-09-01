"""Minimal artwork download abstraction with validation."""

from urllib.request import Request, urlopen

from .artwork_validation import ArtworkPayload, validate_artwork


def download_artwork(url: str, *, timeout: float = 10.0) -> ArtworkPayload:
    request = Request(url, headers={"User-Agent": "Musivex/0.1"})
    with urlopen(request, timeout=timeout) as response:  # noqa: S310 - URL comes from a configured provider.
        data = response.read(10_000_001)
        mime = response.headers.get_content_type()
    return validate_artwork(data, mime)
