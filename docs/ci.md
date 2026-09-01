# Continuous integration

Every push and pull request runs the test suite across Python 3.11, 3.12, and 3.13. The workflow installs Musivex, runs pytest, checks Ruff, and runs mypy against `src`.

Provider credentials and live network access are not required for the normal CI path.