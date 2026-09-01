"""CLI output helpers."""

import json
from typing import Any


def emit_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, default=str))
