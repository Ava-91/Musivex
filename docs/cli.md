# CLI

Musivex exposes the core workflow through a command-line interface.

## Scan

Scan a directory recursively:

```bash
musivex scan ./Music
```

Disable recursion:

```bash
musivex scan ./Music --no-recursive
```

## Preview

Preview the metadata or analysis available for a file:

```bash
musivex preview ./Music/track.mp3
musivex preview ./Music/track.mp3 --json
```

## Tag

The `tag` command is currently safety-oriented and advertises a dry-run operation. Recognition-backed writes should not be treated as fully production-ready until the provider, confidence, and rollback pipeline is complete.

## Scriptable output

Use JSON output where supported when integrating Musivex into scripts. Avoid parsing human-readable output as a stable API while the CLI is still evolving.