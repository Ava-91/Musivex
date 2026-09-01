# Providers

Provider integrations supply external metadata or recognition data. They should remain isolated from the core Musivex models and CLI.

## Provider responsibilities

A provider may supply:

- Recording candidates
- Stable external identifiers
- Track and release metadata
- Artwork
- Other enrichment data supported by its API

## Reliability

Provider failures, timeouts, and rate limits should produce controlled errors rather than corrupting local files. Provider-dependent tests should use mocks or deterministic responses.

## Credentials

Never commit provider tokens or API keys. Prefer environment variables or local configuration mechanisms, and never include real credentials in logs or documentation examples.