"""Metadata provider abstractions."""

from typing import Protocol

from .metadata_model import Metadata


class MetadataProvider(Protocol):
    def search(self, *, title: str, artist: str | None = None) -> list[Metadata]: ...
