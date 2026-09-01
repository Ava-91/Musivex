"""Stage timing utilities for debug diagnostics."""

from contextlib import contextmanager
from time import perf_counter
from typing import Iterator, Callable


@contextmanager
def timed(stage: str, sink: Callable[[str, float], None] | None = None) -> Iterator[None]:
    start = perf_counter()
    try:
        yield
    finally:
        elapsed = perf_counter() - start
        if sink is not None:
            sink(stage, elapsed)
