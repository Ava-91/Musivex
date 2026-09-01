# Recognition

Recognition is the part of Musivex that attempts to determine which recording an audio file represents. It is intentionally separated from metadata writing so an uncertain match cannot silently become a file modification.

## Pipeline

1. Read the input audio file.
2. Analyze the available audio signal.
3. Generate or obtain recognition features.
4. Compare the result with candidate recordings through the configured provider or matching layer.
5. Produce a candidate and confidence information.
6. Apply transformation analysis separately when relevant.
7. Send uncertain results to review instead of automatic writing.

## Confidence

A recognition result should not be treated as authoritative simply because a candidate was returned. Confidence thresholds are used to distinguish results that are safe to automate from results that need review.

## Limitations

Recognition quality depends on the audio source, transformation, available provider data, and matching implementation. Short clips, heavy edits, unusual mixes, or unsupported transformations may produce ambiguous results.

Musivex should prefer a visible uncertain result over a confident-looking false positive.