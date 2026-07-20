# AI201 Open-Source Contribution Journal

## Week 7: Issue Selection

### Selected Issue

**Issue:** [#106 — Shared test fixture for a sample user profile is missing from tests/fixtures](https://github.com/ascherj/pathreview/issues/106)

### Issue Tier

This issue is labeled **Tier 1**, which is appropriate for my current comfort level with the PathReview codebase. I am still learning the repository structure, so a focused test-fixture task gives me an opportunity to understand the project’s testing patterns without changing complex production logic.

### Why I Selected This Issue

I selected this issue because its scope is small and clearly defined. The task is centered on restoring one shared test-data file rather than modifying several services or application features. It also gives me practical experience working with an existing test suite, understanding fixture structure, and making a contribution that can be verified by running tests.

This issue is a good fit for me because I can inspect how the tests load sample profile data, compare the expected schema with existing models and fixtures, and create the missing file using realistic but non-sensitive sample information.

### Problem Summary

The PathReview test suite expects a reusable sample user profile fixture inside the `tests/fixtures/` directory, but that fixture is currently missing.

Because the file is unavailable, tests that depend on the shared sample profile may fail, be skipped, or require duplicated setup data. This makes the test suite less reliable and harder to maintain.

A successful fix would add the missing fixture in the expected location and format. The fixture should contain realistic sample profile data, such as a GitHub username, resume information, and repository examples, so the relevant tests can load the same consistent data and run successfully.
