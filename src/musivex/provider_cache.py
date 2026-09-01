"""Tiny in-memory cache for metadata lookups."""

from .metadata_model import Metadata


class MetadataCache:
    def __init__(self) -> None:
        self._items: dict[tuple[str, str | None], list[Metadata]] = {}

    def get(self, title: str, artist: str | None) -> list[Metadata] | None:
        return self._items.get((title.casefold(), artist.casefold() if artist else None))

    def put(self, title: str, artist: str | None, value: list[Metadata]) -> None:
        self._items[(title.casefold(), artist.casefold() if artist else None)] = value
