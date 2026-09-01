from musivex.metadata_model import Metadata
from musivex.write_plan import plan


def test_plan_contains_only_present_fields() -> None:
    result = plan("track.mp3", Metadata(title="Song", artist="Artist"))
    assert result.changes == {"title": "Song", "artist": "Artist"}
