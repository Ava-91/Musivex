"""Command-line interface for Musivex."""

import argparse
from pathlib import Path

from . import __version__
from .scanner import scan


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="musivex", description="Recognize music and enrich audio metadata.")
    parser.add_argument("--version", action="version", version=f"Musivex {__version__}")
    commands = parser.add_subparsers(dest="command")
    scan_parser = commands.add_parser("scan", help="scan a music folder")
    scan_parser.add_argument("path", type=Path)
    scan_parser.add_argument("--no-recursive", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "scan":
        for item in scan(args.path, recursive=not args.no_recursive):
            print(item.path)
    return 0
