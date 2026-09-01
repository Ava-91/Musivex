"""Enrich normalized recognition results with metadata providers."""

from .metadata_model import Metadata
from .recognition_models import RecognitionResult
from .providers import MetadataProvider


def enrich(result: RecognitionResult, provider: MetadataProvider) -> Metadata | None:
    if not result.title:
        return None
    matches = provider.search(title=result.title, artist=result.artist)
    if not matches:
        return None
    metadata = matches[0]
    metadata.artist = metadata.artist or result.artist
    metadata.album = metadata.album or result.album
    metadata.recording_id = metadata.recording_id or result.recording_id
    metadata.confidence = result.confidence
    return metadata
