"""Human-readable diagnostic formatting."""

from .diagnostics import Diagnostic


def format_diagnostic(diagnostic: Diagnostic) -> str:
    location = f" [{diagnostic.path}]" if diagnostic.path else ""
    provider = f" ({diagnostic.provider})" if diagnostic.provider else ""
    return f"{diagnostic.stage}{provider}{location}: {diagnostic.message}"
