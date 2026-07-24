# PLAN.md

## Issue Summary

Issue G-01 reports that the shared test fixture `tests/fixtures/sample_profiles/basic_profile.json` is missing. The issue description states that multiple integration tests depend on this file and that it should contain a realistic sample portfolio with a GitHub username, resume, and two repositories.

## Root Cause

The `tests/fixtures/sample_profiles/` directory and the `basic_profile.json` fixture do not exist in the repository. A reproduction test confirms that the expected fixture path is missing. The issue manifest and evaluation script also reference this location.

## Files to Change

- `tests/fixtures/sample_profiles/basic_profile.json` (new)
- `tests/integration/test_sample_profile_fixture.py` (reproduction test)

## Implementation Plan

1. Create the `tests/fixtures/sample_profiles/` directory.
2. Add `basic_profile.json` containing:
   - GitHub username
   - Resume information
   - Two sample repositories
3. Verify the reproduction test passes after the fixture is restored.
4. Ensure the change does not introduce any additional failures beyond existing dependency-related errors.

## Verification

- [x] Reproduction test fails before the fix.
- [x] Fixture restored.
- [x] Reproduction test passes after the fix.
- [x] Full test suite run confirms remaining failures are unrelated dependency issues (`ModuleNotFoundError`).