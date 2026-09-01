# CLI

## Scan

```bash
musivex scan ./Music
musivex scan ./Music --no-recursive
```

## Preview

```bash
musivex preview ./Music/track.mp3
musivex preview ./Music/track.mp3 --json
```

## Tag

`tag` currently advertises a dry-run operation. Actual recognition-backed writes will be enabled after the safety and provider pipeline is complete.
