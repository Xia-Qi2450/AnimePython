# AnimePython

**AnimePython is Python, but with anime-themed terminology.**

It is a source-to-source transpiler that converts AnimePython code into regular Python code, allowing the resulting program to run on CPython and use the existing Python ecosystem.

> Python, but we gave it an anime skin.

## Example

AnimePython:

```python
summon random

season Character:
    episode __init__(self, name):
        self.name = name

    episode choose_attack(self):
        ending random.choice([
            "ORA ORA ORA!",
            "DATTEBAYO!",
            "DOMAIN EXPANSION!"
        ])

character = Character("Example")
announce(character.choose_attack())
```

Transpiled Python:

```python
import random

class Character:
    def __init__(self, name):
        self.name = name

    def choose_attack(self):
        return random.choice([
            "ORA ORA ORA!",
            "DATTEBAYO!",
            "DOMAIN EXPANSION!"
        ])

character = Character("Example")
print(character.choose_attack())
```

The goal is that AnimePython programs ultimately behave like ordinary Python programs after transpilation.

## Why?

Because apparently Python wasn't sufficiently weeb.

More seriously, AnimePython is an experiment in programming-language design and source-to-source compilation. Instead of implementing a new runtime, virtual machine, or standard library, AnimePython intends to reuse Python's existing ecosystem.

That means AnimePython can potentially take advantage of:

- CPython
- Python's standard library
- PyPI packages
- Existing Python tooling
- Python's runtime and interpreter

The project is intentionally designed as a **Python-compatible syntax layer**, rather than a completely independent programming language.

## Current Status

AnimePython is currently in early development.

The command-line interface and Python package structure are being established first. The lexer and transpiler are still under development.

The planned compilation pipeline is:

```text
AnimePython source
        │
        ▼
    Tokenizer
        │
        ▼
AnimePython → Python
    transformation
        │
        ▼
   Python source
        │
        ▼
     CPython
```

Initially, the project will rely heavily on Python's existing tokenization and AST facilities rather than implementing an entirely new Python parser.

## Planned Syntax

The exact syntax is still subject to change, but the current idea includes mappings such as:

| Python | AnimePython |
| --- | --- |
| `class` | `season` |
| `def` | `episode` |
| `import` | `summon` |
| `return` | `ending` |
| `if` | `when` |
| `else` | `otherwise` |
| `for` | `montage` |
| `while` | `loop_arc` |
| `try` | `plot_armor` |
| `except` | `plot_twist` |
| `finally` | `post_credits` |
| `print()` | `announce()` |

This vocabulary is expected to evolve as the language develops.

## Installation

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/Xia-Qi2450/AnimePython
cd animepython

python -m pip install -e ".[dev]"
```

The CLI should then be available as:

```bash
animepy
```

Check the installed version with:

```bash
animepy --version
```

## Project Structure

```text
animepython/
├── pyproject.toml
├── README.md
├── src/
│   └── animepython/
│       ├── __init__.py
│       └── cli.py
│
├── tests/
│   ├── test_lexer.py
│   ├── test_transpiler.py
│   └── test_compiler.py
│
└── examples/
    └── hello.ani
```

The project is divided into several planned components:

### Lexer

Responsible for turning AnimePython source code into tokens while preserving Python syntax such as strings, comments, indentation, and operators.

### Transpiler

Responsible for converting AnimePython-specific syntax into equivalent Python syntax.

### Compiler

Responsible for passing the generated Python code to Python's parser/runtime.

### CLI

Provides the `animepy` command used to run AnimePython programs and expose compiler functionality to users.

## Compatibility

AnimePython is intended to generate ordinary Python source code.

For example:

```python
summon numpy
```

would eventually become:

```python
import numpy
```

AnimePython therefore does not need separate AnimePython versions of Python packages. A Python package can remain a normal Python package while AnimePython acts as the syntax layer above it.

## Roadmap

### Phase 1 — Project Foundation

- [x] Package structure
- [x] `pyproject.toml`
- [x] `animepy` CLI entry point
- [ ] Basic test suite
- [ ] Initial documentation

### Phase 2 — Lexer / Token Transformation

- [ ] Tokenize `.apy` source
- [ ] Replace AnimePython keywords with Python equivalents
- [ ] Preserve strings and comments
- [ ] Handle indentation correctly
- [ ] Produce valid Python source

### Phase 3 — Transpilation

- [ ] Parse generated Python with `ast`
- [ ] Validate generated code
- [ ] Improve compiler errors
- [ ] Execute AnimePython files

### Phase 4 — Language Features

- [ ] More syntax mappings
- [ ] AnimePython-specific syntax
- [ ] Better error messages
- [ ] Source mapping between `.apy` and generated `.py`

### Phase 5 — Tooling

- [ ] Syntax highlighting
- [ ] Editor/IDE support
- [ ] Formatter
- [ ] Linter
- [ ] Documentation website

## Philosophy

AnimePython should remain lightweight.

The project should avoid reimplementing functionality that Python already provides unless doing so is necessary for AnimePython-specific features.

The ideal result is:

```text
AnimePython
    ↓
Python
    ↓
CPython
    ↓
The entire Python ecosystem
```

The language can be ridiculous.

The compiler shouldn't have to be.

## License

License information has not yet been decided.
