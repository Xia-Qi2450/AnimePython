"""Lexical analysis for AnimePython source code."""

from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping
from io import StringIO
from tokenize import TokenInfo, generate_tokens
from typing import Final


# Built-in AnimePython syntax.
DEFAULT_KEYWORDS: Final[dict[str, str]] = {
    "season": "class",
    "episode": "def",
    "summon": "import",
    "ending": "return",
    "when": "if",
    "otherwise": "else",
    "montage": "for",
    "loop_arc": "while",
    "plot_armor": "try",
    "plot_twist": "except",
    "post_credits": "finally",
}


class KeywordRegistry:
    """Stores AnimePython keyword replacements.

    A registry starts with the built-in AnimePython syntax and can be
    extended with additional keyword replacements.

    Example:
        registry = KeywordRegistry()
        registry.extend({
            "isekai": "break",
            "flashback": "continue",
        })
    """

    def __init__(
        self,
        keywords: Mapping[str, str] | None = None,
    ) -> None:
        self._keywords: dict[str, str] = dict(DEFAULT_KEYWORDS)

        if keywords is not None:
            self.extend(keywords)

    def add(self, anime_keyword: str, python_keyword: str) -> None:
        """Add or replace a keyword mapping."""
        self._validate_keyword(anime_keyword, python_keyword)
        self._keywords[anime_keyword] = python_keyword

    def extend(self, keywords: Mapping[str, str]) -> None:
        """Add several keyword mappings."""
        for anime_keyword, python_keyword in keywords.items():
            self.add(anime_keyword, python_keyword)

    def resolve(self, word: str) -> str | None:
        """Return the Python equivalent of an AnimePython keyword.

        Returns:
            The replacement keyword, or ``None`` if ``word`` is not
            registered.
        """
        return self._keywords.get(word)

    def __contains__(self, word: str) -> bool:
        """Return whether a word is registered as an AnimePython keyword."""
        return word in self._keywords

    def __getitem__(self, word: str) -> str:
        """Return the Python replacement for a registered keyword."""
        return self._keywords[word]

    def items(self) -> Iterable[tuple[str, str]]:
        """Return all registered keyword mappings."""
        return self._keywords.items()

    @staticmethod
    def _validate_keyword(
        anime_keyword: str,
        python_keyword: str,
    ) -> None:
        """Validate a keyword mapping."""
        if not anime_keyword.isidentifier():
            raise ValueError(
                f"Invalid AnimePython keyword: {anime_keyword!r}"
            )

        if not python_keyword.isidentifier():
            raise ValueError(
                f"Invalid Python keyword replacement: {python_keyword!r}"
            )


def tokenize_source(source: str) -> Iterator[TokenInfo]:
    """Tokenize AnimePython source code.

    AnimePython currently follows Python's lexical rules, so Python's
    standard ``tokenize`` module is used for the actual lexical analysis.

    Args:
        source: AnimePython source code.

    Yields:
        Python ``TokenInfo`` objects.
    """
    yield from generate_tokens(StringIO(source).readline)

def tokenize(source: str) -> list[TokenInfo]:
    """Tokenize source code and return all tokens as a list."""
    return list(tokenize_source(source))