"""Domain errors used by Musivex."""


class MusivexError(Exception):
    """Base exception for expected Musivex failures."""


class UnsupportedFormatError(MusivexError):
    """Raised when an operation receives an unsupported audio format."""


class AudioFileError(MusivexError):
    """Raised when an audio file cannot be inspected safely."""
