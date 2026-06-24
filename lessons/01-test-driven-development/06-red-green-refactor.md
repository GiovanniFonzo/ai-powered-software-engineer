# Step 6: Red, Green, Refactor

## Main Idea

Red-Green-Refactor is the core Test-Driven Development cycle.

    Red -> write a test that fails
    Green -> write the minimum code to make the test pass
    Refactor -> improve the code without changing expected behaviour

## What We Practiced

### Red

The subtract test failed because the subtract function did not exist yet.

### Green

We added the subtract function and pytest returned:

    2 passed

### Refactor

We improved calculator.py by adding:

- type hints
- docstrings
- consistent formatting

The behaviour stayed the same.

After refactoring, pytest still returned:

    2 passed

## Refactoring Rule

During refactoring, do not change expected behaviour.

Run tests before and after the refactor.

If tests fail after refactoring, the cleanup may have introduced a regression.

## Feature vs Refactor

Feature:

    Add multiply() to the calculator.

Refactor:

    Add type hints and docstrings to existing functions.

A feature changes what the software does.

A refactor improves how the code is organised or maintained.

## AI Connection

AI-generated code can work but still be unclear, repetitive, or difficult to maintain.

Refactoring helps us improve naming, documentation, structure, and consistency.

Tests protect the behaviour while we improve the code.

## Python Ignore Rules

We added a .gitignore file to avoid committing generated Python files:

    __pycache__/
    *.pyc
    .pytest_cache/

These files are generated locally and should not be stored in Git.

## Dojo Answers

1. Refactoring means improving the code’s structure, readability, or maintainability without changing its expected behaviour.

2. No. During refactoring, the expected behaviour should not change.

3. We run tests after refactoring to confirm that the code still behaves the same and that the cleanup did not introduce a regression.

4. Adding a feature changes or adds behaviour for the user. Refactoring improves the internal code structure without changing existing behaviour.

5. Refactoring helps when reviewing AI-generated code because AI-generated code may work but still be unclear, repetitive, or difficult to maintain. We can improve its structure while tests confirm the behaviour still works.
