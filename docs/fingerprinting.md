# Acoustic fingerprinting

Musivex keeps its recognition layer provider-neutral. When a provider needs an acoustic fingerprint, the current adapter uses Chromaprint's `fpcalc` executable.

Install Chromaprint/fpcalc separately for local recognition. CI does not require it because recognition-provider tests use mocks.

The existing `fingerprint_file()` helper remains a deterministic content seed and is **not** an acoustic fingerprint.
