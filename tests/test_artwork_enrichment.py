from musivex.artwork_policy_enrichment import should_replace
from musivex.artwork_resolver import cover_art_url


def test_cover_art_url() -> None:
    assert cover_art_url("https://coverart.example", "release") == "https://coverart.example/release/front-500"


def test_existing_artwork_is_preserved_by_default() -> None:
    assert not should_replace(True)
    assert should_replace(True, force=True)
