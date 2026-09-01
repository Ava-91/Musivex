# Supported formats

Musivex is being built around common music-library formats. Support is format-specific because containers store metadata differently.

| Format | Scanning | Metadata read/write | Notes |
| --- | --- | --- | --- |
| MP3 | Yes | Supported | ID3 metadata |
| FLAC | Yes | Supported | Vorbis comments |
| M4A / MP4 | Yes | Supported | MP4 metadata atoms |
| WAV | Yes | Limited / evolving | Container metadata varies |

Recognition and artwork capabilities may have different requirements from basic scanning and metadata access.

## Important

A format being scannable does not mean every metadata field or transformation workflow is equally supported. Check the implementation and tests before relying on a specific field in automation.