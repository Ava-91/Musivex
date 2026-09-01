"""Serialize benchmark measurements as stable JSON."""
import json
from pathlib import Path

def write_report(result: dict[str, object], path: str | Path) -> None:
    Path(path).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
