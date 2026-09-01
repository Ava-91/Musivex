from musivex.confidence import assess
from musivex.metadata_model import Metadata
from musivex.recognition import Candidate
from musivex.review_queue import ReviewQueue


def test_review_queue_only_accepts_ambiguous_matches() -> None:
    queue = ReviewQueue()
    candidate = Candidate(Metadata(title="Song"), 0.7)
    queue.add(candidate, assess(candidate.score))
    assert queue.pop()[0] is candidate
    queue.add(candidate, assess(0.2))
    assert queue.pop() is None
