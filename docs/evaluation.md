# Evaluation

Musivex's recognition work should be evaluated separately from metadata writing.

## Evaluation goals

Measure:

- Recording identification accuracy
- Transformation classification accuracy
- Confidence calibration
- False-positive rate
- False-negative rate
- Runtime and memory behavior

## Transformation coverage

The evaluation suite should include deterministic fixtures for original, slowed, sped-up, reverb, slowed + reverb, sped-up + reverb, and unrelated or ambiguous audio where legally redistributable test data is available.

## Reproducibility

Evaluation inputs and expected labels should be deterministic. Do not depend on live provider responses for baseline CI results.

Benchmark results should be treated separately from recognition quality metrics so a faster system is not automatically considered a more accurate one.