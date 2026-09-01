"""Resolve artwork URLs from normalized metadata."""

from urllib.parse import urljoin


def cover_art_url(base: str, release_id: str) -> str:
    return urljoin(base.rstrip("/") + "/", f"{release_id}/front-500")
