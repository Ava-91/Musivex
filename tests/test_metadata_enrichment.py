from musivex.metadata_enrichment import enrich
from musivex.metadata_model import Metadata
from musivex.recognition_models import RecognitionResult


class Provider:
    def search(self, *, title: str, artist: str | None = None) -> list[Metadata]:
        return [Metadata(title=title, artist=artist, album="Album")]


def test_enrichment_carries_recognition_identity() -> None:
    result = enrich(RecognitionResult("Song", "Artist", confidence=0.9), Provider())
    assert result is not None
    assert result.artist == "Artist"
    assert result.album == "Album"
    assert result.confidence == 0.9
