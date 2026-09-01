# Evaluation corpus

Musivex keeps evaluation metadata and generators in the repository, but does not commit copyrighted songs.

The manifest covers original recordings, slowed and sped-up variants, slowed+reverb, sped-up+reverb, pitch-shifted variants, unrelated recordings, and ambiguous candidates.

Use `tests/evaluation_manifest.json` as the expected-label source and generate local WAV fixtures with `musivex.fixture_generator.write_tone` when running experiments.

Recognition accuracy and transformation accuracy should be reported separately. False positives and false negatives should be tracked rather than hiding them behind one aggregate score.
