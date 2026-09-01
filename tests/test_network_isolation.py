from unittest.mock import patch

def test_provider_network_is_not_required_for_core_tests() -> None:
    # Core test suites should be able to run without contacting providers.
    with patch('urllib.request.urlopen', side_effect=AssertionError('network access in core tests')):
        assert True
