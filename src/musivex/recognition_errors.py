"""Errors raised by recognition providers."""


class RecognitionError(Exception):
    """Base class for recognition failures."""


class RecognitionConfigurationError(RecognitionError):
    """Provider configuration is missing or invalid."""


class RecognitionTransportError(RecognitionError):
    """A provider could not be reached or returned an invalid response."""


class RecognitionNoMatch(RecognitionError):
    """The provider processed the audio but found no match."""
