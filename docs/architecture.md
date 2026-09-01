# Architecture

Musivex is organized around a small core pipeline: file scanning -> audio analysis/recognition -> normalized metadata -> optional enrichment -> safe writing.

The CLI is an interface layer and should not contain recognition or metadata business logic. Provider integrations are isolated so they can be mocked during tests and replaced independently.
