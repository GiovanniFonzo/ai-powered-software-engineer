# Step 9: Integration Tests

## Main Idea

An integration test checks that multiple parts of the system work together correctly.

A unit test checks one small piece of code in isolation.

An integration test checks a workflow or connection between multiple parts.

## Unit Test vs Integration Test

Unit test:

    Tests one function alone.

Integration test:

    Tests multiple functions or components working together.

## Calculator Example

In the calculator exercise, the integration-style test checks a workflow that uses both add() and subtract().

Workflow:

    Start with 10
    Add 5
    Subtract 3
    Final result should be 12

This uses:

    add()
    subtract()

The test passed with:

    7 passed

## PHP Support Case System Connection

In the PHP Support Case System, an integration test for /cases would connect:

- route
- model
- view

Example:

    /cases receives the request
    the model loads the cases
    the view renders the case list

This matters because some bugs only appear when components work together.

## Why Integration Tests Matter

Integration tests matter because each function can work correctly alone, but the combined workflow can still fail.

Many real bugs happen between components.

## AI Connection

Integration tests are useful when AI changes code across multiple files.

AI may update a route, a model, and a view.

An integration test confirms the connected parts still work together after the change.

## Dojo Answers

1. An integration test checks that multiple parts of the system work together correctly.

2. A unit test checks one small piece of code in isolation. An integration test checks a workflow or connection between multiple parts.

3. Integration tests matter because some bugs only appear when components work together. Each function may pass alone, but the combined workflow can still fail.

4. In the calculator exercise, a workflow using add() and subtract() is closer to an integration test because it checks both functions working together in one workflow.

5. In the PHP Support Case System, an integration test for /cases would connect the route, the model, and the view: the route receives the request, the model loads the cases, and the view renders the case list.

6. Integration tests are useful when AI changes code across multiple files because they confirm the connected parts still work together after the change.
