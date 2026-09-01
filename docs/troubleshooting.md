# Troubleshooting

## No files are found
Check the path and ensure the extension is supported.

## A match is uncertain
Use preview/review mode instead of writing tags automatically. Lowering confidence thresholds can increase false positives.

## A provider fails
Check provider configuration, credentials, rate limits, and network access. Core tests do not require a live provider.

## A write is refused
Check whether the target container supports the requested metadata field and whether dry-run mode is enabled.