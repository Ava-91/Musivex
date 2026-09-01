"""Small JSON rollback journal for safe batch operations."""

from dataclasses import asdict, dataclass
import json
from pathlib import Path


@dataclass(frozen=True, slots=True)
class BackupRecord:
    original: str
    backup: str


def save_record(record: BackupRecord, journal: str | Path) -> Path:
    path = Path(journal)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(record), indent=2) + "\n", encoding="utf-8")
    return path


def load_record(journal: str | Path) -> BackupRecord:
    data = json.loads(Path(journal).read_text(encoding="utf-8"))
    return BackupRecord(original=str(data["original"]), backup=str(data["backup"]))
