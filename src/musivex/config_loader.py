"""Load and validate simple TOML configuration."""
from pathlib import Path
import tomllib
from .configuration import MusivexConfig

def load_config(path: str | Path | None = None) -> MusivexConfig:
    config = MusivexConfig()
    if path is None:
        config.validate()
        return config
    with Path(path).expanduser().open("rb") as handle:
        values = tomllib.load(handle)
    merged = {**config.__dict__, **values}
    if "cache_dir" in merged:
        merged["cache_dir"] = Path(str(merged["cache_dir"])).expanduser()
    result = MusivexConfig(**merged)
    result.validate()
    return result
