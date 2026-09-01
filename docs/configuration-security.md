# Configuration security

Provider credentials should be supplied through environment variables or local configuration that is excluded from version control. Musivex must never print secret values in normal or debug logs.

Configuration precedence is: built-in defaults < configuration file < explicit CLI/runtime overrides.

The example configuration contains no credentials and is safe to commit.