"""Basic calibration metrics."""


def mean_confidence(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def accuracy_at_threshold(predictions: list[tuple[float, bool]], threshold: float) -> float:
    if not predictions:
        return 0.0
    correct = sum((confidence >= threshold) == expected for confidence, expected in predictions)
    return correct / len(predictions)
