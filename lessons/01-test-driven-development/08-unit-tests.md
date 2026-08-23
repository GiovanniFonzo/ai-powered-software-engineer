# Step 8: Unit Tests

## Main Idea

A unit test checks one small piece of code in isolation.

In the calculator project, we are unit testing:

    add()
    subtract()

Unit tests are the bottom layer of the Testing Pyramid.

They should usually be:

- small
- fast
- focused
- easy to understand

## Why Unit Tests Matter

A unit test should prove one specific behavior.

Example:

    add(2, 3) should return 5

But one test is not always enough.

A function can work for one case and fail for another.

That is why we added multiple scenarios.

## Practical Example

We expanded the calculator test suite from two tests to six tests.

The tests now check:

- add positive numbers
- add negative numbers
- add zero
- subtract positive numbers
- subtract negative numbers
- subtract to zero

After running pytest, the result was:

    6 passed

## PHP Support Case System Connection

In the PHP Support Case System, a good unit test could check:

    find_case_by_id(2) returns the correct support case

This is a unit test because it checks one specific piece of logic.

## AI Connection

Unit tests are useful with AI-generated code because they give fast feedback.

AI can generate code that looks correct but still behaves incorrectly.

Unit tests prove whether each small function actually behaves as expected.

## Dojo Answers

1. A unit test checks one small piece of code in isolation, usually one function or method.

2. A unit test should be small and focused because it should prove one specific behavior. This makes the test easier to understand, faster to run, and easier to debug when it fails.

3. It is useful to test more than one scenario for the same function because a function can work for one input but fail for another. For example, add(2, 3) may work, but we also want to check negative numbers and zero.

4. In the calculator project, we are unit testing the add() and subtract() functions.

5. In the PHP Support Case System, find_case_by_id() could become a unit test because it checks one specific piece of logic: finding the correct support case by ID.

6. Unit tests are useful when using AI-generated code because they give fast feedback. AI can write code that looks correct, but unit tests prove whether each small function actually behaves as expected.
