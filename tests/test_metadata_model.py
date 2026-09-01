from musivex.metadata_model import Metadata, Transformation
from musivex.validation import validate


def test_metadata_serializes_nested_values() -> None:
    metadata = Metadata(title="Example", transformation=Transformation(slowed=True, reverb=True))
    data = metadata.as_dict()
    assert data["title"] == "Example"
    assert data["transformation"]["slowed"] is True


def test_invalid_confidence_is_reported() -> None:
    assert validate(Metadata(confidence=1.5)) == ["confidence must be between 0 and 1"]
