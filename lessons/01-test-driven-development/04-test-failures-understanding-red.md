# Step 4: Test Failures / Understanding Red

## Main Idea

In Test-Driven Development, Red means the test failed.

A failing test is not automatically bad. It is useful feedback.

It helps us understand:

- what test failed
- what result was expected
- what result actually happened
- where the problem is located

## Example Failure

We changed the calculator test from:

    assert result == 5

to:

    assert result == 6

Then pytest showed:

    assert 5 == 6

This means:

    Actual result: 5
    Expected result: 6

In this case, the function was correct because 2 + 3 equals 5.

The test was wrong because it expected 6.

## Why This Matters

When a test fails, we should not panic.

We should read the failure message carefully and ask:

1. What did the code actually return?
2. What did the test expect?
3. Is the code wrong?
4. Is the test wrong?
5. What is the smallest fix?

## AI Connection

This is important when working with AI-generated code.

AI can write code that looks correct but behaves incorrectly.

A failing test gives us clear feedback instead of relying only on how the code looks.

The test failure helps us decide whether the AI-generated code is wrong, whether the test is wrong, or whether the requirement was unclear.

## Dojo Answers

1. Red means the test failed. In TDD, this is expected when we first write a test for behavior that is not working yet.

2. No. A failing test is useful feedback because it helps us reproduce the issue and understand what needs to be fixed.

3. When reading a pytest failure, we compare the actual result with the expected result.

4. If add(2, 3) returns 5 but the test expected 6, the test is wrong because 2 + 3 should equal 5.

5. Reading test failures is useful when AI writes code because AI can make mistakes. The failure message shows what was expected, what actually happened, and where the mismatch is.
