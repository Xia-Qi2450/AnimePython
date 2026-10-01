"""AnimePython - Python, but with anime terminology."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("animepython")
except PackageNotFoundError:
    # Useful when running directly from a source checkout.
    __version__ = "0.0.0.dev0"

__all__ = ["__version__"]