"""Evaluation metrics for recognition and transformation classifiers."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EvaluationMetrics:
    total: int
    correct: int
    false_positives: int
    false_negatives: int

    @property
    def accuracy(self) -> float:
        return self.correct / self.total if self.total else 0.0


def classification_metrics(expected: list[bool], predicted: list[bool]) -> EvaluationMetrics:
    if len(expected) != len(predicted):
        raise ValueError("expected and predicted lengths differ")
    correct = sum(a == b for a, b in zip(expected, predicted))
    false_positives = sum(not a and b for a, b in zip(expected, predicted))
    false_negatives = sum(a and not b for a, b in zip(expected, predicted))
    return EvaluationMetrics(len(expected), correct, false_positives, false_negatives)
