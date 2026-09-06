from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
lesson_path = ROOT / "lessons/01-test-driven-development/15-fixtures.md"

content = """# Step 15 — Fixtures

## Main Idea

A fixture is reusable test setup.

Instead of repeating the same setup inside many tests, we define the setup once and reuse it.

Key memory:

    Fixture = reusable test setup

## Why Fixtures Matter

Fixtures help keep tests:

    cleaner
    shorter
    less repeated
    easier to update
    easier to understand

When many tests repeat the same setup, the test suite becomes harder to maintain.

If the setup needs to change, we may need to update many tests.

A fixture solves this by keeping the setup in one place.

## Pytest Fixture Syntax

In pytest, we create a fixture using:

    @pytest.fixture

Example:

    import pytest

    @pytest.fixture
    def positive_numbers():
        return 3, 4

A test can use the fixture by accepting it as a function parameter:

    def test_multiply_returns_product_of_two_positive_numbers(positive_numbers):
        first_number, second_number = positive_numbers

        result = multiply(first_number, second_number)

        assert result == 12

## Practical Example

In this step, we added a fixture called positive_numbers.

The fixture returns:

    3, 4

Then we reused it in tests for:

    add()
    multiply()

The full test suite passed:

    10 passed

## Why This Helps with AI

Fixtures make tests clearer for both humans and AI.

When AI is asked to add or refactor tests, fixtures show the reusable setup clearly.

This reduces repeated code and makes the test suite easier to extend safely.

## Connection to PHP Support Case System

In the PHP Support Case System, fixtures could be used for:

    sample support case
    sample case list
    fake form submission
    invalid form data
    case with status New
    case with status In Progress
    case with status Resolved

This would make tests for create, list, detail, and status update features easier to maintain.

## Dojo Answers

1. A fixture in testing is reusable setup data or setup code that can be shared by multiple tests.

2. Fixtures are useful because they reduce repetition and keep tests cleaner, shorter, and easier to understand.

3. When many tests repeat the same setup, the test suite becomes harder to maintain. If the setup needs to change, we may need to update many tests, which increases the chance of mistakes.

4. A fixture makes tests easier to maintain because the setup is defined once. If the setup changes, we update the fixture instead of editing every test.

5. In pytest, the decorator used to create a fixture is @pytest.fixture.

6. In the calculator project, we could create a fixture for reusable input numbers, for example two positive numbers like 3 and 4, or a reusable calculator data set.

7. In the PHP Support Case System, a fixture could create a sample support case, a fake form submission, a test case list, a case with status New, or a case with invalid/missing fields.
"""

lesson_path.write_text(content, encoding="utf-8")
print(f"Wrote {lesson_path}")
