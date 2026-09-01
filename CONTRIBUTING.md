# Contributing to Musivex

Thanks for helping improve Musivex.

## Development workflow

1. Find or open an issue describing the change.
2. Split substantial work into sub-issues when the pieces can be completed independently.
3. Create a focused branch such as `feature/12-cli`, `fix/96-benchmark-import`, or `docs/20-documentation`.
4. Make small, meaningful commits.
5. Add or update tests for behavior changes.
6. Run the local checks before opening a pull request.
7. Open a pull request against `main` and reference the issue with `Closes #N` when appropriate.
8. Address CI or review feedback before merging.

## Local checks

```bash
python -m pytest
ruff check .
mypy src
```

## Commit style

Prefer clear prefixes such as:

- `feat:` for new behavior
- `fix:` for bug fixes
- `test:` for tests
- `docs:` for documentation
- `refactor:` for internal restructuring
- `ci:` for automation
- `perf:` for performance work

## Pull requests

Keep PRs focused on one logical change. Update documentation when user-visible behavior changes. Never commit API keys, credentials, private data, or copyrighted audio fixtures.
