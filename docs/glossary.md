# Glossary

## Test-Driven Development

A development workflow where tests are written before the implementation code.

## Red-Green-Refactor

The core TDD cycle:

1. Red: write a failing test.
2. Green: write the simplest code that passes.
3. Refactor: clean the code while keeping tests passing.

## Unit Test

A test that checks a small isolated part of the code.

## Integration Test

A test that checks whether multiple parts of a system work together.

## End-to-End Test

A test that checks a full user workflow from start to finish.

## Continuous Integration

A practice where tests are run automatically when code changes are pushed.

## Project File Types

### .py files

Python files are used for application code and test code.

Examples:

    src/calculator.py
    tests/test_calculator.py

### .md files

Markdown files are used for documentation, lesson notes, dojo answers, and project summaries.

Examples:

    README.md
    docs/glossary.md
    lessons/01-test-driven-development/11-continuous-integration.md

### .yml files

YAML files are used for automation and configuration instructions for tools like GitHub Actions.

Example:

    .github/workflows/python-tests.yml

In this project, the .yml workflow tells GitHub Actions to set up Python, install pytest, and run the test suite automatically.
