"""Command-line interface for AnimePython."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    """Build and return the AnimePython argument parser."""
    parser = argparse.ArgumentParser(
        prog="animepy",
        description="Run AnimePython source files.",
    )

    parser.add_argument(
        "file",
        type=Path,
        nargs="?",
        help="AnimePython source file (.ani).",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the AnimePython CLI and return an exit status."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.file is None:
        parser.print_help()
        return 0

    if not args.file.exists():
        print(
            f"animepy: error: file not found: {args.file}",
            file=sys.stderr,
        )
        return 2

    if not args.file.is_file():
        print(
            f"animepy: error: not a file: {args.file}",
            file=sys.stderr,
        )
        return 2

    if args.file.suffix != ".ani":
        print(
            f"animepy: error: expected a .ani file, got {args.file.suffix!r}",
            file=sys.stderr,
        )
        return 2

    print(f"AnimePython source: {args.file}")
    print("Compiler not implemented yet.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())