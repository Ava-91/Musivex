"""Artwork replacement policy and cache keys."""

from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True, slots=True)
class ArtworkPolicy:
    replace_existing: bool = False
    max_bytes: int = 10_000_000


def cache_key(identifier: str, url: str) -> str:
    return sha256(f"{identifier}\0{url}".encode("utf-8")).hexdigest()
