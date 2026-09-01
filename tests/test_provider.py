from musivex.cache import TTLCache
from musivex.metadata_model import Metadata
from musivex.providers import MetadataProvider


def test_cache_round_trip() -> None:
    cache = TTLCache()
    cache.set("song", [Metadata(title="Song")])
    assert cache.get("song")[0].title == "Song"


def test_provider_protocol_shape() -> None:
    class Fake:
        def search(self, *, title: str, artist: str | None = None):
            return [Metadata(title=title, artist=artist)]

    provider: MetadataProvider = Fake()
    assert provider.search(title="Song")[0].title == "Song"
