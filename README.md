# Musivex

Automatic music metadata enrichment and transformation-aware song recognition.

Musivex is an early-stage Python project for scanning music files, reading and normalizing metadata, analyzing tracks, and safely preparing metadata updates. Recognition and transformation-aware features are being developed incrementally.

## Current capabilities

- Recursive audio-file scanning
- Supported-format detection
- Normalized metadata models
- Metadata reading and safe writing primitives
- CLI commands for scanning and previewing files
- Dry-run-oriented tagging flow
- Recognition and transformation components under active development
- Automated tests, linting, type checking, and benchmarks

## Quick start

```bash
python -m pip install -e .
python -m pytest
musivex --help
musivex scan ./Music
```

See [`docs/quickstart.md`](docs/quickstart.md) for a fuller walkthrough.

## Documentation

- [Quick start](docs/quickstart.md)
- [CLI](docs/cli.md)
- [Architecture](docs/architecture.md)
- [Recognition](docs/recognition.md)
- [Supported formats](docs/supported-formats.md)
- [Configuration and security](docs/configuration-security.md)
- [Testing](docs/testing.md)
- [Evaluation](docs/evaluation.md)
- [CI](docs/ci.md)
- [Troubleshooting](docs/troubleshooting.md)

## Development

Musivex uses a standard Python `src/` layout. Install it in editable mode, run the test suite, and use the project tooling before opening a pull request.

```bash
python -m pip install -e .
python -m pytest
ruff check .
mypy src
```

## Safety and limitations

Musivex is designed to avoid silently applying uncertain metadata. Recognition-backed writes should remain reviewable, and destructive operations should use the project's safety mechanisms. Do not commit private credentials or copyrighted audio fixtures to the repository.

## Status

**Early development.** Interfaces and recognition behavior may change while the core engine is stabilized.

## License

MIT License. See [`LICENSE`](LICENSE).
