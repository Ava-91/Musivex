"""Errors raised by metadata providers."""


class ProviderError(Exception):
    """Base provider failure."""


class ProviderUnavailable(ProviderError):
    """Provider could not be reached or used."""


class RateLimited(ProviderError):
    """Provider requested slower requests."""
