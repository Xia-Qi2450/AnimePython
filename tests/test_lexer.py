from tokenize import COMMENT, INDENT, NAME, STRING

import pytest

from animepython.lexer import (
    DEFAULT_KEYWORDS,
    KeywordRegistry,
    tokenize,
    tokenize_source,
)


def test_default_keywords_exist() -> None:
    registry = KeywordRegistry()

    assert registry.resolve("season") == "class"
    assert registry.resolve("episode") == "def"
    assert registry.resolve("summon") == "import"


def test_unknown_word_is_not_a_keyword() -> None:
    registry = KeywordRegistry()

    assert registry.resolve("Miku") is None


def test_custom_keywords_can_be_added() -> None:
    registry = KeywordRegistry()

    registry.add("isekai", "break")

    assert registry.resolve("isekai") == "break"


def test_custom_keywords_can_be_added_in_bulk() -> None:
    registry = KeywordRegistry()

    registry.extend(
        {
            "isekai": "break",
            "flashback": "continue",
        }
    )

    assert registry.resolve("isekai") == "break"
    assert registry.resolve("flashback") == "continue"


def test_custom_keywords_do_not_modify_defaults() -> None:
    registry = KeywordRegistry()

    registry.add("isekai", "break")

    assert "isekai" not in DEFAULT_KEYWORDS


def test_invalid_anime_keyword_is_rejected() -> None:
    registry = KeywordRegistry()

    with pytest.raises(ValueError):
        registry.add("not-valid!", "break")


def test_invalid_python_replacement_is_rejected() -> None:
    registry = KeywordRegistry()

    with pytest.raises(ValueError):
        registry.add("isekai", "not-valid!")


def test_tokenize_keywords_as_names() -> None:
    tokens = tokenize("season Character:")

    assert tokens[0].type == NAME
    assert tokens[0].string == "season"

    assert tokens[1].type == NAME
    assert tokens[1].string == "Character"


def test_strings_remain_strings() -> None:
    tokens = tokenize('announce("season episode summon")')

    string_tokens = [
        token
        for token in tokens
        if token.type == STRING
    ]

    assert len(string_tokens) == 1
    assert string_tokens[0].string == '"season episode summon"'


def test_comments_remain_comments() -> None:
    tokens = tokenize("# season should not be replaced")

    comments = [
        token
        for token in tokens
        if token.type == COMMENT
    ]

    assert len(comments) == 1
    assert comments[0].string == "# season should not be replaced"


def test_indentation_is_preserved() -> None:
    source = """\
season Character:
    episode greet(self):
        announce("Hello!")
"""

    tokens = tokenize(source)

    assert any(token.type == INDENT for token in tokens)


def test_tokenize_source_is_lazy() -> None:
    tokens = tokenize_source("season Character:")

    # The function returns an iterator instead of eagerly building a list.
    assert iter(tokens) is tokens