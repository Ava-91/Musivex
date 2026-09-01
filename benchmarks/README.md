# Benchmarks

The benchmark helpers are importable as the `benchmarks` package so that the benchmark test suite behaves consistently in local development and GitHub Actions.

Run the benchmark tests with:

```bash
PYTHONPATH=. pytest tests/test_benchmarks.py
```

The CI workflow sets the same import path explicitly.
