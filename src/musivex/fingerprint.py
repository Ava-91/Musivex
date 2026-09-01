"""Local fingerprint primitives used by recognition providers."""

from hashlib import sha256
from pathlib import Path


def fingerprint_file(path: str | Path, *, sample_bytes: int = 1_048_576) -> str:
    """Return a stable content fingerprint seed.

    This is intentionally a provider-neutral seed, not a claim of acoustic
    fingerprinting. Real acoustic fingerprints can be supplied by providers.
    """
    with Path(path).open("rb") as handle:
        data = handle.read(sample_bytes)
    return sha256(data).hexdigest()
