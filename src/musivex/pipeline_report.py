"""Human-readable pipeline result formatting."""

from .end_to_end import PipelineResult


def summary(result: PipelineResult) -> str:
    if result.recognition is None:
        return "No match"
    name = " — ".join(part for part in (result.recognition.title, result.recognition.artist) if part)
    action = "safe to apply" if result.should_write else "review required"
    return f"{name or 'Unknown'} ({result.recognition.confidence:.0%}; {action})"
