"""Policy for preserving canonical metadata while naming variants."""

from .metadata_model import Metadata
from .naming import variant_title


def apply_variant_title(metadata: Metadata) -> Metadata:
    if metadata.title:
        metadata.title = variant_title(metadata.title, metadata.transformation)
    return metadata
