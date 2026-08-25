# Step 10: End-to-End Tests

## Main Idea

An end-to-end test checks a full user journey from start to finish.

A unit test checks one small function.

An integration test checks connected internal parts.

An end-to-end test checks whether the user can complete the full workflow successfully.

## Unit vs Integration vs End-to-End

Unit test:

    Does one function work?

Integration test:

    Do multiple parts work together?

End-to-end test:

    Can the user complete the full task?

## Calculator Example

In the calculator exercise, we simulated an end-to-end-style user journey.

Workflow:

    User starts with 100
    User adds 50
    User subtracts 25
    User sees final result 125

After running pytest, the result was:

    8 passed

## PHP Support Case System Connection

In the PHP Support Case System, an end-to-end test could check:

    User opens /cases/new
    User fills the support case form
    User submits the form
    User is redirected
    User sees the new case listed on /cases

This is different from an integration test because it checks the full task from the user perspective.

## Conditional Workflow Note

If a form has multiple conditional rulesets, we should test the important user journeys.

Example:

    User selects Individual -> personal fields appear -> submit succeeds
    User selects Company -> company fields appear -> submit succeeds
    User misses a required conditional field -> validation error appears

We do not always test every possible combination end-to-end because that can become too large.

A good strategy is:

    Unit tests for individual rules
    Integration tests for rule + form rendering + validation
    End-to-end tests for the most important user journeys

## Why End-to-End Tests Matter

End-to-end tests are useful because they catch problems that only appear in the full user journey, such as:

- form submission problems
- redirect problems
- validation problems
- missing output
- broken navigation
- user-facing workflow errors

## Why Fewer End-to-End Tests

End-to-end tests are powerful, but they are usually:

- slower
- more fragile
- more complex
- more expensive to maintain

That is why the Testing Pyramid usually has fewer end-to-end tests than unit tests.

## AI Connection

End-to-end tests are useful when AI changes a user-facing workflow.

They confirm that the full task still works for the user, not only the internal code pieces.

## Dojo Answers

1. An end-to-end test checks a full user journey from start to finish.

2. A unit test checks one small function or method in isolation. An end-to-end test checks the full task from the user’s perspective.

3. An integration test checks connected internal parts, such as route + model + view. An end-to-end test checks whether the user can complete the full workflow successfully.

4. End-to-end tests are useful because they catch problems that only appear in the full user journey, such as form submission, redirects, validation errors, missing output, or broken navigation.

5. We usually have fewer end-to-end tests because they are slower, more fragile, more complex, and more expensive to maintain.

6. In the PHP Support Case System, a full end-to-end test could check that a user opens /cases/new, fills the support case form, submits it, gets redirected, and sees the new case listed on /cases.

7. End-to-end tests are useful when AI changes a user-facing workflow because they confirm that the full task still works for the user, not only the internal code pieces.
