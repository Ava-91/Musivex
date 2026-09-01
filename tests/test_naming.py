from musivex.metadata_model import Transformation
from musivex.naming import variant_title


def test_variant_title_is_composed_once() -> None:
    transformation = Transformation(slowed=True, reverb=True)
    assert variant_title("Song (Slowed + Reverb)", transformation) == "Song (Slowed + Reverb)"


def test_original_title_is_unchanged() -> None:
    assert variant_title("Song", Transformation()) == "Song"
