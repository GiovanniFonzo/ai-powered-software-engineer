# Step 11: Continuous Integration

## Main Idea

Continuous Integration, or CI, means tests run automatically when code changes are pushed to a shared repository.

So far, we have been running pytest manually:

    python3 -m pytest

That is useful, but it depends on the developer remembering to run the tests.

CI makes the test check automatic.

## Manual Testing vs CI

Manual testing:

    Developer changes code
    Developer remembers to run pytest
    Developer pushes code

Continuous Integration:

    Developer pushes code
    GitHub starts an automated workflow
    Dependencies are installed
    pytest runs automatically
    GitHub reports pass or fail

## Why CI Matters

CI protects the project from silent breakages.

If a change breaks a test, the failure appears automatically.

This helps teams avoid merging or releasing broken code.

## Current Project Connection

The AI-Powered Software Engineer repo currently has:

    6 unit tests
    1 integration-style test
    1 end-to-end-style test

Total:

    8 pytest tests

With CI, GitHub can run these tests automatically when code is pushed.

## PHP Support Case System Connection

For the PHP Support Case System, CI could later run checks for:

- routes
- model logic
- case workflows
- form submission behavior
- status update behavior

This would help catch regressions before changes are merged or released.

## AI Connection

CI is especially useful with AI-generated code.

AI can change multiple files quickly.

CI gives us an automatic safety check to confirm that the generated or refactored code still passes the test suite.

## CI Workflow Concept

    Local code change
        |
        v
    git push
        |
        v
    GitHub repository
        |
        v
    CI workflow starts
        |
        v
    Install dependencies
        |
        v
    Run pytest
        |
        v
    Pass or fail result

## Dojo Answers

1. CI stands for Continuous Integration.

2. The main purpose of Continuous Integration is to run checks automatically when code changes are pushed, so broken code can be caught early.

3. So far, we have been running pytest manually on our Mac with python3 -m pytest.

4. CI will automatically run the test suite when code is pushed to GitHub.

5. CI is useful when working with AI-generated code because AI can change multiple files quickly. CI gives us an automatic safety check to confirm the generated code still passes the tests.

6. In this project, CI should run python3 -m pytest inside the exercises/tdd-python-pytest folder.

7. CI is useful before pushing or merging bigger project changes because it helps catch regressions before broken code becomes part of the main branch.
