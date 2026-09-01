# Troubleshooting

## `musivex` is not found

Install the project in editable mode from the repository root:

```bash
python -m pip install -e .
```

## Tests fail during collection

Check that the development environment is using the project's supported Python version and that the package was installed correctly. Run:

```bash
python -m pytest
```

## A file is skipped

Check whether its extension is supported and whether the file can be read. One problematic file should not prevent a library scan from continuing.

## Recognition is uncertain

Treat low-confidence or ambiguous matches as review candidates. Do not force metadata onto a file just to make the library look complete.

## CI fails

Reproduce the failing command locally where possible. Check tests first, then lint and type checking. Keep CI independent of live provider services and private credentials.