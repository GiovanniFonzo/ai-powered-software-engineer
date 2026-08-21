# Step 7: The Testing Pyramid

## Main Idea

The Testing Pyramid is a way to organize tests by size, speed, and cost.

At the bottom, we have many small tests.

At the top, we have fewer large tests.

    End-to-End Tests
    Integration Tests
    Unit Tests

## Unit Tests

A unit test checks one small piece of code in isolation.

In the calculator example:

    add(2, 3) should return 5
    subtract(10, 4) should return 6

These are unit tests because they test one function at a time.

Unit tests are usually:

- fast
- small
- cheap to run
- easy to debug

## Integration Tests

An integration test checks that multiple parts of the system work together.

For the PHP Support Case System, an integration test could check:

    /cases route loads the case model
    /cases route passes cases to the view
    /cases page renders the expected case list

Integration tests are useful because many bugs happen between components.

## End-to-End Tests

An end-to-end test checks a full user journey.

For the PHP Support Case System, an end-to-end test could check:

    User opens /cases/new
    User fills the support case form
    User submits the form
    User sees the new case listed

End-to-end tests are powerful, but they are usually slower and more expensive to maintain.

## Pyramid Rule

A healthy test suite usually has:

    Many unit tests
    Some integration tests
    Few end-to-end tests

This keeps the test suite fast, useful, and maintainable.

## Why This Matters for AI-Assisted Development

AI can generate code quickly, but different test levels check different kinds of correctness.

Unit tests check:

    Did the function work?

Integration tests check:

    Did the parts connect correctly?

End-to-end tests check:

    Did the user workflow work?

This helps us trust AI-generated or AI-refactored code more safely.

## PHP Support Case System Examples

Unit test:

    find_case_by_id(2) returns the correct support case

Integration test:

    /cases loads the model and renders the cases page

End-to-end test:

    A user opens /cases/new, submits a case, and sees it listed

## Dojo Answers

1. The Testing Pyramid organizes tests into levels: many fast unit tests at the bottom, some integration tests in the middle, and fewer end-to-end tests at the top.

2. Unit tests are at the bottom of the pyramid.

3. A unit test checks one small piece of code in isolation.

4. An integration test checks that multiple parts of the system work together.

5. An end-to-end test checks a full user journey from start to finish.

6. We usually have fewer end-to-end tests because they are slower, more complex, more fragile, and more expensive to maintain.

7. In the PHP Support Case System, a unit test could check that find_case_by_id(2) returns the correct support case.

8. In the PHP Support Case System, an integration test could check that /cases loads the case model and renders the case list page correctly.

9. In the PHP Support Case System, an end-to-end test could check that a user opens /cases/new, submits a new support case, and then sees the new case listed on /cases.
