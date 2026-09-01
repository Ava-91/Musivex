# Configuration and security

Musivex is designed to keep configuration separate from source code and credentials.

## Configuration principles

Use configuration for behavior such as recognition thresholds, provider settings, artwork behavior, backups, caching, and naming preferences as those options become available in the implementation.

Prefer this precedence when multiple sources exist:

```text
built-in defaults → configuration file → environment → CLI override
```

The exact available keys should follow the current configuration model; unknown keys should be rejected rather than silently ignored.

## Secrets

Never commit API keys, access tokens, passwords, or private configuration to Git.

Use placeholders in examples:

```text
MUSIVEX_PROVIDER_TOKEN=your-token-here
```

Do not print secrets in logs or diagnostic output.

## File safety

Use dry-run and backup/rollback mechanisms before bulk metadata changes. Musivex should fail safely when a write cannot be completed.