from musivex.metadata_model import Metadata, Transformation
from musivex.title_policy import apply_variant_title


def test_policy_updates_only_title() -> None:
    metadata = Metadata(title="Song", artist="Artist", transformation=Transformation(sped_up=True))
    result = apply_variant_title(metadata)
    assert result.title == "Song (Sped Up)"
    assert result.artist == "Artist"
