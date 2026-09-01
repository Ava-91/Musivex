# Recognition normalization

Provider responses are converted into `RecognitionResult` before entering the rest of the pipeline. Missing fields are represented as `None`, confidence is clamped to `0..1`, and provider-specific identifiers remain available in `raw`.
