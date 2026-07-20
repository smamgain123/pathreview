## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/106

**Issue title:** Shared test fixture for a sample user profile is missing from tests/fixtures/

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**

The test suite is missing a shared sample user profile fixture that multiple integration tests depend on. As a result, tests either duplicate setup logic or cannot run because the expected fixture no longer exists. The fix is to restore a reusable sample profile fixture so tests can consistently use the same realistic test data, making the test suite easier to maintain and more reliable.

**Issue selection notes ("Is this issue right for me?"):**

I chose this issue because it is a Tier 1 issue with a clearly defined scope and estimated effort of one to two hours. It focuses on improving the project's test infrastructure rather than modifying production code, making it a good first contribution to a larger codebase. The affected files are clearly identified, and the expected outcome is straightforward to verify.

**Branch name:** test/106-shared-user-profile-fixture

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [x] Issue added to cohort ledger