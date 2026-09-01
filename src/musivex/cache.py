"""Tiny in-memory provider cache."""

from dataclasses import dataclass, field
from time import monotonic


@dataclass
class TTLCache:
    ttl_seconds: float = 3600
    _values: dict[str, tuple[float, object]] = field(default_factory=dict)

    def get(self, key: str) -> object | None:
        item = self._values.get(key)
        if item is None:
            return None
        created, value = item
        if monotonic() - created >= self.ttl_seconds:
            self._values.pop(key, None)
            return None
        return value

    def set(self, key: str, value: object) -> None:
        self._values[key] = (monotonic(), value)
