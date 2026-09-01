"""Apply explicit CLI-style configuration overrides."""
from dataclasses import replace
from .configuration import MusivexConfig

def apply_overrides(config: MusivexConfig, **overrides: object) -> MusivexConfig:
    clean = {key: value for key, value in overrides.items() if value is not None}
    if "cache_dir" in clean:
        from pathlib import Path
        clean["cache_dir"] = Path(str(clean["cache_dir"])).expanduser()
    result = replace(config, **clean)
    result.validate()
    return result
