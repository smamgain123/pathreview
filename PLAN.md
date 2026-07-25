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

# Issue Summary

Issue G-01 reports that the shared fixture
`tests/fixtures/sample_profiles/basic_profile.json`
is missing. Multiple integration tests expect this file.
The fixture should contain a realistic sample profile including a GitHub username,
resume information, and two repositories.

---

# Inputs

- Existing repository structure
- Issue description
- Expected fixture location:
  `tests/fixtures/sample_profiles/basic_profile.json`
- Required profile fields:
  - GitHub username
  - Resume
  - Two repositories

# Outputs

- New file:
  `tests/fixtures/sample_profiles/basic_profile.json`
- Reproduction test that validates the fixture exists
- Passing reproduction test after the fixture is restored

---

# Files to Modify

- `tests/fixtures/sample_profiles/basic_profile.json`
- `tests/integration/test_sample_profile_fixture.py`

---

# Risks / Unknowns

- The exact JSON schema expected by future integration tests is not enforced in the current repository.
- The fixture must contain realistic field names that match the issue description.
- Future tests may validate the JSON structure, not just file existence.
- Existing dependency-related test failures (missing packages such as `structlog`) are unrelated and should not be mistaken for regressions caused by this fix.

---

# Investigation

Before implementing:

1. Search the repository for references to `basic_profile.json`.
2. Inspect `scripts/issues_manifest.json`.
3. Inspect `scripts/run_evals.py`.
4. Verify whether any existing tests load this fixture.
5. Create a failing reproduction test before implementing the fix.

---

# Edge Cases

- The fixture directory does not exist.
- The fixture file exists but contains invalid JSON.
- Required keys (`github_username`, `resume`, `repositories`) are missing.
- The repository list contains fewer than two repositories.
- Future tests load the fixture using a relative path.

---

# Implementation Plan

1. Create `tests/fixtures/sample_profiles/`.
2. Restore `basic_profile.json`.
3. Populate it with realistic sample data.
4. Run the reproduction test.
5. Confirm the test passes.

---

# Verification

- [x] Reproduction test fails before implementation.
- [x] Fixture restored.
- [x] Reproduction test passes.
- [x] Full test suite run confirms remaining failures are unrelated dependency issues.