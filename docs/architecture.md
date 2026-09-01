# Architecture

Musivex is organized as a small pipeline with clear boundaries between file handling, audio analysis, metadata, providers, and the user interface.

```text
music directory
    ↓
scanner
    ↓
file/audio model
    ↓
metadata reader + audio analysis
    ↓
recognition / transformation analysis
    ↓
normalized metadata + confidence
    ↓
optional provider enrichment
    ↓
preview / review
    ↓
safe metadata writer
```

## Design principles

- The CLI is an interface layer, not the home of recognition or metadata business logic.
- Provider integrations are isolated so they can be mocked, replaced, and tested independently.
- Metadata is normalized before it reaches format-specific writers.
- Recognition results should carry enough information for safe review before writing.
- File operations should fail per file where possible rather than terminating an entire batch.

## Main areas

- `src/musivex/`: application package and core models.
- `tests/`: unit and integration coverage.
- `benchmarks/`: deterministic performance fixtures and benchmark runners.
- `docs/`: user and developer documentation.

The project is still in early development, so module boundaries and APIs may evolve.