# Step 16 — Parameterization

## Main Idea

Parameterization means running the same test logic with many different input and expected output examples.

Key memory:

    Parameterization = one test, many examples

Instead of writing many separate test functions, we can write one test and provide multiple test cases.

## Why Parameterization Matters

Parameterization helps make tests:

    less repeated
    easier to extend
    easier to read
    better for edge cases
    more maintainable

It reduces repeated test code.

Instead of copying the same test structure many times, we keep one test and pass different data into it.

## Pytest Parameterization Syntax

In pytest, parameterized tests use:

    @pytest.mark.parametrize

Example:

    @pytest.mark.parametrize(
        "first_number, second_number, expected",
        [
            (2, 3, 5),
            (-2, -3, -5),
            (10, 0, 10),
        ],
    )
    def test_add_returns_expected_sum(first_number, second_number, expected):
        result = add(first_number, second_number)

        assert result == expected

This means pytest runs the same test once for each example.

## Practical Example

In this step, we refactored calculator tests for:

    add()
    subtract()
    multiply()

Instead of many separate repeated tests, we used parameterized examples.

The full test suite passed:

    13 passed

## Why This Helps with Edge Cases

Parameterization makes it easy to add more examples.

For example:

    zero
    negative numbers
    same numbers
    invalid inputs
    missing fields
    boundary values

This is useful because edge cases often reveal bugs that normal examples miss.

## Why This Helps with AI

When using AI to generate or change code, parameterized tests give AI a clearer contract.

The test data shows multiple examples of expected behavior.

This makes it harder for AI-generated code to pass only one simple case while failing other cases.

## Connection to PHP Support Case System

In the PHP Support Case System, parameterization could be useful for testing:

    valid case creation
    missing subject
    missing description
    invalid priority
    different case statuses
    existing case IDs
    missing case IDs
    invalid routes

This would let us test many form and route scenarios without writing repeated test functions.

## Dojo Answers

1. Parameterization in testing means running the same test logic with different input and expected output examples.

2. Parameterization is useful because it lets us test many scenarios without writing many repeated test functions.

3. Parameterization reduces repeated test code. Instead of copying the same test structure again and again, we keep one test and pass different data into it.

4. In pytest, the decorator used for parameterized tests is @pytest.mark.parametrize.

5. Parameterization is good for edge cases because we can easily add more examples to the test data list, such as zero, negative numbers, empty values, missing fields, or invalid inputs.

6. In the calculator project, add(), subtract(), and multiply() are all good candidates for parameterized tests because each function can be tested with different number combinations and expected results.

7. In the PHP Support Case System, scenarios that could be parameterized include valid case creation, missing subject, missing description, invalid priority, different case statuses, existing case IDs, missing case IDs, and invalid routes.
