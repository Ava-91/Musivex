# Continuous integration

Musivex runs automated checks for pull requests so regressions are caught before changes are merged.

## Current checks

The CI workflow installs the project and runs:

```bash
python -m pytest
ruff check .
mypy src
```

The test matrix covers the Python versions configured by the repository workflow.

## Keeping CI deterministic

Normal CI should not require proprietary audio, personal files, API credentials, or live external provider responses. Provider-dependent behavior should be mocked or isolated behind deterministic tests.

A failing CI job should be fixed before merging unless the failure is explicitly understood and documented.