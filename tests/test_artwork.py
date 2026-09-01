from pathlib import Path

import pytest

from musivex.artwork import read_artwork
from musivex.artwork_policy import ArtworkPolicy, cache_key
from musivex.artwork_validation import validate_artwork


def test_read_artwork_returns_none_for_unknown_file(tmp_path: Path) -> None:
    path = tmp_path / "empty.bin"
    path.write_bytes(b"x")
    assert read_artwork(path) is None


def test_valid_artwork_is_accepted() -> None:
    payload = validate_artwork(b"image", "image/jpeg")
    assert payload.mime_type == "image/jpeg"


def test_invalid_artwork_type_is_rejected() -> None:
    with pytest.raises(ValueError, match="unsupported artwork"):
        validate_artwork(b"image", "image/gif")


def test_artwork_size_limit_is_enforced() -> None:
    with pytest.raises(ValueError, match="size limit"):
        validate_artwork(b"12345", "image/png", max_bytes=4)


def test_policy_defaults_to_preserving_existing_artwork() -> None:
    assert ArtworkPolicy().replace_existing is False


def test_cache_key_is_stable() -> None:
    assert cache_key("mbid", "https://example.test/a") == cache_key("mbid", "https://example.test/a")
