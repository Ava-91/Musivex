from musivex import __version__
from musivex.cli import build_parser


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_cli_parser() -> None:
    parser = build_parser()
    assert parser.prog == "musivex"
