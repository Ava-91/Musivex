from pathlib import Path

def test_ci_workflow_exists() -> None:
    workflow = Path('.github/workflows/ci.yml')
    assert workflow.exists()
    text = workflow.read_text(encoding='utf-8')
    assert 'pytest' in text
    assert 'pull_request' in text
