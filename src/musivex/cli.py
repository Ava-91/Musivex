"""Command-line entry point for Musivex."""

import argparse

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="musivex",
        description="Recognize music and enrich audio metadata.",
    )
    parser.add_argument("--version", action="version", version=f"Musivex {__version__}")
    return parser


def main() -> int:
    build_parser().parse_args()
    return 0
