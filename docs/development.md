# Development

## Setup

```bash
python -m pip install -e .
```

## Validate changes

```bash
python -m pytest
ruff check .
mypy src
```

## Workflow

Keep changes focused on one issue. For substantial work, use sub-issues, a dedicated branch, meaningful commits, and a pull request against `main`.

## Repository boundaries

Core behavior belongs in the package, not in CLI-only code. External providers should remain isolated behind testable interfaces. Tests should not require private music libraries or live credentials.