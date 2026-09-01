# Transformations

Musivex treats a transformed copy as the same underlying recording plus additional audio characteristics when the evidence supports that conclusion.

## Target transformations

- Original
- Slowed
- Sped up
- Pitch shifted
- Reverb
- Slowed + reverb
- Sped up + reverb

The transformation model is intentionally separate from recording identity. This lets Musivex answer two questions independently:

```text
What recording is this?
What was done to this version?
```

## Limitations

Speed, pitch, reverb, edits, and mastering differences can overlap with naturally different recordings. Transformation detection should therefore expose confidence and should not override an uncertain recording match.