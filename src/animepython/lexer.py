"""Lexer for AnimePython source code."""

from __future__ import annotations

from io import StringIO
from tokenize import TokenInfo, generate_tokens
from typing import Iterator


def tokenize_source(source: str) -> Iterator[TokenInfo]:
    """Tokenize AnimePython source code.

    AnimePython currently follows Python's lexical rules, so the standard
    library's ``tokenize`` module provides the underlying lexer.

    Args:
        source: AnimePython source code.

    Yields:
        Python ``TokenInfo`` objects.
    """
    yield from generate_tokens(StringIO(source).readline)