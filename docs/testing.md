# Testing

Musivex uses automated tests to protect file handling, metadata behavior, recognition boundaries, CLI behavior, and safety features.

## Local checks

```bash
python -m pytest
ruff check .
mypy src
```

## Test categories

- Unit tests for models and small components
- Metadata read/write round-trip tests
- Scanner and format tests
- Recognition and transformation tests
- CLI tests
- Benchmark and evaluation tests

## Test data

Tests should use synthetic, generated, public-domain, or otherwise redistributable fixtures. Do not commit commercial music or other copyrighted recordings merely to make recognition tests convenient.

Provider-dependent tests should use mocks or deterministic fixtures so normal CI does not require external services.

## CI

Pull requests are checked automatically. A change should not be considered complete until the relevant tests and static checks pass.