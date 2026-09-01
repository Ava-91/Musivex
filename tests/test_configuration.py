from pathlib import Path
import pytest
from musivex.configuration import MusivexConfig
from musivex.config_loader import load_config
from musivex.config_overrides import apply_overrides

def test_defaults_are_valid() -> None:
    MusivexConfig().validate()

def test_loader_reads_toml(tmp_path: Path) -> None:
    config_file = tmp_path / "musivex.toml"
    config_file.write_text('confidence_threshold = 0.9\ndry_run = false\n', encoding="utf-8")
    config = load_config(config_file)
    assert config.confidence_threshold == 0.9
    assert config.dry_run is False

def test_overrides_do_not_mutate_source() -> None:
    original = MusivexConfig()
    changed = apply_overrides(original, confidence_threshold=0.7)
    assert original.confidence_threshold == 0.85
    assert changed.confidence_threshold == 0.7

def test_invalid_threshold_is_rejected() -> None:
    with pytest.raises(ValueError):
        MusivexConfig(confidence_threshold=2).validate()
