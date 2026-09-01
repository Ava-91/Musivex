from pathlib import Path

from musivex.fingerprint import fingerprint_file
from musivex.matching import best_match
from musivex.metadata_model import Metadata
from musivex.recognition import Candidate


def test_fingerprint_is_stable(tmp_path: Path) -> None:
    path = tmp_path / "sample.bin"
    path.write_bytes(b"audio")
    assert fingerprint_file(path) == fingerprint_file(path)


def test_best_match_returns_highest_score() -> None:
    low = Candidate(Metadata(title="low"), 0.2)
    high = Candidate(Metadata(title="high"), 0.9)
    assert best_match([low, high]).metadata.title == "high"
