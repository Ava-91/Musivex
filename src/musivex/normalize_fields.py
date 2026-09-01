"""Field aliases used by recognition providers."""

ALIASES = {
    "recording_id": ("recording_id", "isrc", "id"),
    "release_id": ("release_id", "upc", "release"),
}


def first_present(payload: dict[str, object], names: tuple[str, ...]) -> object | None:
    for name in names:
        if payload.get(name) is not None:
            return payload[name]
    return None
