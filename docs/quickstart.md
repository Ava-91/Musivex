# Quick start

## Install

Musivex currently uses a standard Python `src/` layout.

```bash
python -m pip install -e .
```

## Verify the installation

```bash
musivex --help
python -m pytest
```

## Scan a library

```bash
musivex scan ./Music
```

Disable recursive traversal when needed:

```bash
musivex scan ./Music --no-recursive
```

## Preview a file

```bash
musivex preview ./Music/track.mp3
musivex preview ./Music/track.mp3 --json
```

## Tagging

The current tagging command is intentionally safety-oriented. Recognition-backed writes are still being developed, so preview and dry-run behavior should be preferred while the provider and rollback pipeline evolves.
