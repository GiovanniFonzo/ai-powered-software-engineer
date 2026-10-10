from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
lesson_path = ROOT / "lessons/01-test-driven-development/18-diagnosing-failures-and-scaling-testing.md"

content = """# Step 18 — Diagnosing Failures and Scaling Testing

## Main Idea

As a project grows, tests will fail more often.

The skill is not only writing tests.

The skill is knowing how to diagnose failures quickly.

Key memory:

    Diagnosing failures = understand the failure before changing code

A failing test is not a disaster.

A failing test is information.

## Questions to Ask When Pytest Fails

When pytest fails, check:

    Which test failed?
    What was expected?
    What actually happened?
    Did the test fail because the code is wrong?
    Did the test fail because the test is wrong?
    Is the failure isolated or does it affect many tests?

## Expected Result vs Actual Result

The expected result is what the test says should happen.

The actual result is what the code really returned.

Example:

    assert 123.0 == 125.0

This means:

    actual result = 123.0
    expected result = 125.0

Then we diagnose:

    Is the code wrong?
    Or is the test expectation wrong?

## Practical Example

In this step, we intentionally changed the tax service test expectation from:

    assert result == 123.0

to:

    assert result == 125.0

Pytest failed with:

    assert 123.0 == 125.0

This showed that the code returned 123.0, but the test expected 125.0.

Diagnosis:

    The code was correct.
    The test expectation was wrong.

After fixing the test back to:

    assert result == 123.0

the single test file passed:

    1 passed

Then the full test suite passed:

    14 passed

## Scaling Testing

Scaling testing means using good habits as the test suite grows.

Useful habits include:

    run all tests before pushing
    run one test file when debugging
    run one specific test when needed
    use clear test names
    use fixtures to reduce repeated setup
    use parameterization for many scenarios
    use mocking for external dependencies
    use CI to check everything on GitHub

## Useful Pytest Commands

Run all tests:

    python3 -m pytest

Run one test file:

    python3 -m pytest tests/test_tax_service.py

Run one specific test:

    python3 -m pytest tests/test_tax_service.py::test_calculate_total_with_tax_uses_mocked_tax_rate

Show more detailed output:

    python3 -m pytest -v

Stop after first failure:

    python3 -m pytest -x

## Why This Helps with AI

When AI changes code, tests may fail.

The engineer should not immediately accept AI's next fix.

Instead, diagnose the failure first:

    read the failing test
    compare expected and actual result
    decide if the code or test is wrong
    make the smallest safe fix
    rerun the relevant test
    rerun the full suite

This keeps AI-assisted development controlled and safe.

## Connection to PHP Support Case System

In the PHP Support Case System, diagnosing failures would help when tests fail for:

    creating a case
    listing cases
    showing case details
    updating status
    handling missing fields
    handling invalid routes
    handling missing case IDs

The same diagnosis process applies:

    Which test failed?
    What was expected?
    What actually happened?
    Is the route, model, view, data, or test expectation wrong?

## Dojo Answers

1. A failing test is useful because it gives us information. It shows that something does not match the expected behavior, so we can investigate, improve, and fix the problem.

2. When pytest fails, we should first check which test failed, what was expected, what actually happened, whether the code is wrong, whether the test is wrong, and whether the failure is isolated or affects many tests.

3. The expected result is what the test says should happen. The actual result is what the code really returned. Diagnosis means comparing the two and deciding whether the code is wrong or the test is wrong.

4. We should not immediately change the code when a test fails because we might misunderstand the failure and break something else, especially as the project grows.

5. Clear test names help because they explain the behavior being tested. When a test fails, the name helps us understand quickly what part of the system or behavior is broken.

6. The command to run one specific test file is:

    python3 -m pytest tests/test_tax_service.py

The command to run one specific test inside that file is:

    python3 -m pytest tests/test_tax_service.py::test_calculate_total_with_tax_uses_mocked_tax_rate

7. In a large project, CI is useful because it runs the full test suite automatically on GitHub. This helps catch problems before broken code is merged or shared.
"""

lesson_path.write_text(content, encoding="utf-8")
print(f"Wrote {lesson_path}")
