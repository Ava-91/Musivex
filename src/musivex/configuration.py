"""Configuration models and defaults for Musivex."""
from dataclasses import dataclass, field
from pathlib import Path

@dataclass(frozen=True)
class MusivexConfig:
    confidence_threshold: float = 0.85
    dry_run: bool = True
    embed_artwork: bool = True
    backup_before_write: bool = True
    naming_template: str = "{title}"
    cache_dir: Path = field(default_factory=lambda: Path.home() / ".cache" / "musivex")
    provider: str = "auto"

    def validate(self) -> None:
        if not 0.0 <= self.confidence_threshold <= 1.0:
            raise ValueError("confidence_threshold must be between 0 and 1")
        if not self.naming_template.strip():
            raise ValueError("naming_template must not be empty")
        if not self.provider.strip():
            raise ValueError("provider must not be empty")
