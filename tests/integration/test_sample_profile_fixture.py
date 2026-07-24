"""Reproduce Issue #106: the shared sample profile fixture is missing."""

from pathlib import Path


def test_basic_profile_fixture_exists() -> None:
    """The shared sample profile fixture required by integration tests must exist."""
    fixture_path = Path("tests/fixtures/sample_profiles/basic_profile.json")

    assert fixture_path.exists(), (
        "Missing shared fixture: " "tests/fixtures/sample_profiles/basic_profile.json"
    )
