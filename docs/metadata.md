# Metadata

Musivex separates normalized metadata from format-specific storage.

## Common fields

- Title
- Artist
- Album
- Album artist
- Release date or year
- Track and disc numbers
- Genre
- External identifiers
- Artwork
- Detected transformation
- Recognition confidence

Missing metadata should be represented explicitly rather than causing a scan to fail.

## Transformations

A detected transformation is additional information about the audio. For example, a track can represent the canonical recording while also being classified as slowed and reverberated. Transformation information should not overwrite the canonical recording identity.

## Writing

Format-specific writers are responsible for translating normalized fields into the container's tagging system. Existing unrelated metadata should be preserved where practical, and writes should remain reviewable and safe.