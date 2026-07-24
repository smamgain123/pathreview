## Week 7: Issue Selection

**Issue link:** https://github.com/ascherj/pathreview/issues/106

**Issue title:** Shared test fixture for a sample user profile is missing from tests/fixtures/

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

### Problem summary

The project is missing a shared sample profile fixture that tests expect to find inside `tests/fixtures/`. Without this fixture, tests that rely on sample profile data may fail, require duplicated setup data, or be unable to load the expected input. A successful fix will add the fixture in the correct location and use the exact field structure expected by the existing tests. This will allow the tests to reuse consistent sample data and run reliably.

### Is this issue right for me?

* [x] I can identify the likely files involved: `tests/fixtures/`, the tests that load the fixture, and any schema or model that defines profile fields.
* [x] The issue has a focused scope and does not require changing complex production logic.
* [x] I can reproduce or inspect the failure by searching for references to the missing sample profile fixture.
* [x] I can estimate the work at approximately one to two hours.
* [x] I have the prerequisites needed: the project runs locally, the test suite is available, and I can run `pytest`.
* [x] I know how to verify the fix: run the relevant tests and confirm the fixture loads without errors.
* [x] This Tier 1 issue matches my current comfort level with the codebase.

### Selection notes

I selected this issue because it has a small and clearly defined scope. Before implementing it, I will trace the tests that consume the missing fixture to determine the required filename, data format, and fields rather than guessing. The task should mainly involve adding or correcting test data, so it is appropriate for my current familiarity with PathReview. I estimate the work will take one to two hours, including inspecting existing fixtures, implementing the file, and running the relevant tests.

**Branch name:** `test/106-shared-user-profile-fixture`

**Setup confirmation:** [x] The application runs locally.

**Cohort ledger confirmation:** [x] Issue #106 is recorded in the cohort issue ledger.

# Week 8: Implementation

## Reproduction

I first reproduced the issue by creating an integration test that asserted the existence of `tests/fixtures/sample_profiles/basic_profile.json`. The test failed with an AssertionError because the fixture did not exist, confirming the issue before making any changes.

**Reproduction commit:** `9de7652`

---

## Root Cause

The repository was missing the shared fixture file referenced by the issue description. The issue manifest and evaluation script both referenced `tests/fixtures/sample_profiles/basic_profile.json`, but the directory and file were absent.

---

## Fix

I created the missing directory and restored `basic_profile.json` with a realistic sample profile containing:
- GitHub username
- Resume information
- Two sample repositories

This matches the requirements described in the issue.

**Fix commit:** `4c66e22`

---

## Verification

- ✅ Reproduction test failed before the fix.
- ✅ Reproduction test passed after restoring the fixture.
- ✅ Ran the full test suite.
- ✅ Remaining failures were unrelated `ModuleNotFoundError` dependency issues already present in the local environment.

---

## Reflection

This issue reinforced the importance of reproducing a bug before implementing a fix. Rather than creating files based on assumptions, I traced references in the repository, confirmed the expected location and structure, wrote a failing reproduction test, and then restored only the missing fixture. This resulted in a small, targeted change with clear verification.