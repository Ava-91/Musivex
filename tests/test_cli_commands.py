from musivex.cli import build_parser


def test_cli_exposes_core_commands() -> None:
    parser = build_parser()
    for command in ("scan", "preview", "tag"):
        args = parser.parse_args([command, "music.mp3"])
        assert args.command == command
