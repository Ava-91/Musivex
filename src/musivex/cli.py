"""Command-line interface for Musivex."""

import argparse
from pathlib import Path

from . import __version__
from .cli_output import emit_json
from .reader import read_metadata
from .scanner import scan


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="musivex", description="Recognize music and enrich audio metadata.")
    parser.add_argument("--version", action="version", version=f"Musivex {__version__}")
    commands = parser.add_subparsers(dest="command")
    scan_parser = commands.add_parser("scan", help="scan a music folder")
    scan_parser.add_argument("path", type=Path)
    scan_parser.add_argument("--no-recursive", action="store_true")
    preview = commands.add_parser("preview", help="preview existing metadata")
    preview.add_argument("path", type=Path)
    preview.add_argument("--json", action="store_true")
    tag = commands.add_parser("tag", help="prepare a tagging operation")
    tag.add_argument("path", type=Path)
    tag.add_argument("--dry-run", action="store_true", default=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "scan":
        for item in scan(args.path, recursive=not args.no_recursive):
            print(item.path)
    elif args.command == "preview":
        metadata = read_metadata(args.path).as_dict()
        if args.json:
            emit_json(metadata)
        else:
            for key, value in metadata.items():
                print(f"{key}: {value}")
    elif args.command == "tag":
        print(f"Dry-run tagging: {args.path}")
    return 0
