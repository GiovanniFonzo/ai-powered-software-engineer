# Step 1: Course Introduction + Lesson Overview

## Main Idea

AI can generate code quickly, but tests help engineers trust, ship, and maintain that code safely.

This course focuses on using engineering discipline around AI-assisted software development.

## Key Concept

Without tests, we often follow this workflow:

    Write code -> run manually -> hope it works

With Test-Driven Development, we follow this workflow:

    Write test -> see it fail -> write code -> see it pass -> refactor

## Red-Green-Refactor

### Red

Write a test for behavior that does not exist yet. The test fails.

### Green

Write the simplest code that makes the test pass.

### Refactor

Clean the code while keeping the test passing.

## Why This Matters for My Projects

### PHP Support Case System

Tests can protect routes, case creation, case listing, and status workflows.

### Flask Blogging App

Tests can protect API responses, database behavior, and endpoint contracts.

### prod-platform

Tests can protect health checks, monitoring logic, and service status reporting.

## AI Connection

AI-generated code is not automatically safe or correct.

Tests act as a contract between the requirement and the implementation.

Instead of asking AI to simply generate code, I can define expected behavior through tests and use AI to help implement code that satisfies those tests.

## Dojo Questions

1. Why is being careful not enough when changing software?
2. What does TDD stand for?
3. In TDD, do we write the test before or after the code?
4. What does the Red step mean?
5. What does the Green step mean?
6. What does Refactor mean?
7. Why are tests especially important when using AI-generated code?
8. In the PHP Support Case System, what is one thing we could test first?
