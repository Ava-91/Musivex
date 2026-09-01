# Testing

Musivex tests are designed to be deterministic. Provider/network behavior should be mocked in normal CI. Audio fixtures should be synthetic or openly licensed and committed only when redistribution is permitted.

Run locally with `pytest`. CI additionally runs Ruff and mypy.