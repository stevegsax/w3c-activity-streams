"""Smoke tests to verify the package is importable and dependencies are wired up."""

import w3c_activity_streams


def test_version() -> None:
    assert w3c_activity_streams.__version__ == "0.1.0"


def test_dependencies_importable() -> None:
    import alembic  # noqa: F401
    import pydantic  # noqa: F401
    import sqlalchemy  # noqa: F401
