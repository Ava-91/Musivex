# Recognition behavior

Recognition should identify the underlying recording first and treat transformations such as slowed, sped-up, reverb, and pitch shifts as attributes of that recording.

Matches should include confidence. High-confidence matches may be eligible for automatic enrichment; ambiguous matches belong in the review flow.

Provider APIs may differ in coverage and rate limits. Musivex should expose provider failures clearly and avoid pretending that an uncertain match is correct.