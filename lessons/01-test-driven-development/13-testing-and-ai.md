# Step 13 — Testing and AI

## Main Idea

AI can generate code fast, but tests define whether the code is correct.

The safe engineering workflow is not:

    Ask AI for code
    Copy code
    Hope it works

The safer workflow is:

    Define expected behavior
    Write tests
    Ask AI to help implement or refactor
    Run pytest locally
    Push to GitHub
    Let GitHub Actions run CI
    Review before accepting

## Why This Matters

AI-generated code can look correct because it may have good naming, comments, and structure.

However, it can still:

    miss edge cases
    change existing behavior
    break a workflow
    ignore validation rules
    overcomplicate simple code
    introduce reliability or security risks

The final judge should be:

    tests + CI + human review

## Tests as a Contract

Tests act like a contract because they describe what the code must do.

AI can help write the implementation, but the code must satisfy the tests before it is accepted.

In this step, we added multiply() using the TDD workflow.

First, the test expected multiply() to exist.

Pytest failed with:

    ImportError: cannot import name 'multiply'

That was the Red step.

Then we added the implementation:

    def multiply(first_number: int | float, second_number: int | float) -> int | float:
        """Return the product of two numbers."""
        return first_number * second_number

Pytest then passed with:

    10 passed

That was the Green step.

## Role of CI

CI runs the test suite automatically after changes are pushed to GitHub.

This protects the project because it confirms the full test suite still passes outside the local machine.

## Role of the Human Engineer

The human engineer is still responsible for:

    reviewing AI-generated code
    checking that tests are meaningful
    confirming that requirements are covered
    deciding whether the code is safe to accept

AI can assist, but the engineer approves.

## Dojo Answers

1. We should not trust AI-generated code only because it looks correct because AI can produce code that has good naming, comments, and structure but still contains hidden bugs, missed edge cases, or broken behavior.

2. Tests should define correctness when using AI to write code. The expected behavior should be written as tests before we trust the implementation.

3. Tests act like a contract for AI-generated code because they describe what the code must do. AI can help write the implementation, but the code must satisfy the tests before we accept it.

4. CI runs the test suite automatically after AI changes are pushed to GitHub. It confirms whether the full project still passes, not just the file we changed locally.

5. The human engineer still has responsibility to review the AI-generated code, understand the changes, check that the tests are meaningful, and decide whether the code is safe to accept.

6. In this project, our safety checks are local pytest, unit tests, integration-style tests, end-to-end-style tests, GitHub Actions CI, and human review.

7. In the PHP Support Case System, this workflow could help when adding /cases/create by defining tests first for valid case creation, missing required fields, invalid data, redirect behavior, and whether the new case appears in the case list. Then AI can help implement the route, but tests and CI verify the behavior.

## Key Memory

    AI can generate.
    Tests verify.
    CI protects.
    Engineer approves.
