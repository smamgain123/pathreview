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


### Check-in 2 (end-of-week)

**Branch:**
`test/106-shared-user-profile-fixture`

**Pull Request:**
https://github.com/smamgain123/pathreview/pull/1

**What I built:**
Completed Issue #106 by restoring the missing shared sample profile fixture (`tests/fixtures/sample_profiles/basic_profile.json`) and adding an integration test to verify that the fixture exists and can be loaded successfully. I also updated the project documentation in `PLAN.md` and `JOURNAL.md`.

**Tests modified:**
- `tests/integration/test_sample_profile_fixture.py`

**What the tests cover:**
The integration test verifies that the shared sample profile fixture exists at the expected location and can be loaded successfully. This prevents regressions where the fixture is accidentally removed, renamed, or omitted from future changes.

**Self-review:**
- [x] Ran `make check` (only pre-existing repository lint failures unrelated to this issue remain)
- [x] Ran `make test-unit` (only pre-existing repository test failures unrelated to this issue remain)

**Work completed:**

- Restored the missing shared sample profile fixture.
- Added a reproduction integration test.
- Verified the new fixture test passes independently.
- Ran repository verification commands and documented existing unrelated failures.
- Opened a draft pull request summarizing the implementation and testing.

**Testing performed:**

- `pytest -v tests/integration/test_sample_profile_fixture.py`
  - ✅ 1 test passed
- `make check`
  - Repository contains pre-existing lint issues unrelated to this change.
- `make test-unit`
  - Repository contains pre-existing failing tests unrelated to this change.

**Reflection:**

This project reinforced the importance of reproducing an issue before fixing it, verifying the fix with a focused regression test, and documenting repository-wide issues separately from changes introduced by the current work.


## Week 10 — Iteration & reflection

### Reviewer feedback

**Feedback received:** [ ] Yes  [x] No — still awaiting review

**Summary of feedback:**

No reviewer or maintainer feedback was received during the Summer 2026 offering. My pull request remained open, so there were no review comments to address before completing the module.

**How you responded:**

N/A.

---

### Reflection

**What was harder than you expected?**

The hardest part was understanding how the issue fit into a codebase that I did not write. My issue looked simple at first, but I needed to trace references to `tests/fixtures/sample_profiles/basic_profile.json` through files like `scripts/issues_manifest.json` and `scripts/run_evals.py` before I understood what the fixture was expected to contain. I also had to separate repository-wide issues from problems related to my own change.

**What did you learn about working in a large codebase?**

I learned that reading existing code is just as important as writing new code. Before implementing the fix, I searched the repository to understand where the missing fixture was referenced and how it would be used. This experience showed me that making a small, well-tested change is often more valuable than making a large change without understanding the surrounding code.

**How did AI tools help — and where did they fall short?**

AI was very helpful for navigating an unfamiliar repository, creating a structured implementation plan, and explaining the purpose of different files. It also helped me organize my documentation and think through edge cases. However, AI could not determine the expected fixture structure on its own—I still had to inspect the repository, read the issue description, and verify my assumptions by running the tests locally.

**What would you do differently if you started over?**

If I started over, I would spend more time reading the contribution guidelines and PR template before writing any code. Earlier in the project I lost points because my documentation did not exactly match the required template. I also would have created my reproduction test earlier because it made it much easier to verify that the final implementation solved the correct problem.

**What are you most proud of from this module?**

I am most proud of following a complete open-source contribution workflow instead of only writing code. I reproduced the issue, documented an implementation plan, restored the missing shared fixture, added an integration test, created a pull request with testing instructions, and kept my journal updated throughout the four-week process. That gave me experience with the same development process used in real software teams.