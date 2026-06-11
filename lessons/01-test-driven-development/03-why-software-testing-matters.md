# Step 2: Why Software Testing Matters

## Main Idea

Software testing matters because software changes all the time.

A feature can work today, but after one small change, something that used to work can break.

That kind of break is called a regression.

## What Is a Regression?

A regression is when existing behavior stops working after a code change.

Example:

    /cases works today

Later, we add:

    /cases/create

But if the route logic is changed incorrectly, the old /cases page might stop working.

A test helps catch that problem before the code is committed or shipped.

## Why Manual Checking Is Not Enough

Manual checking means opening the browser, clicking pages, or running commands by hand.

This is useful, but it does not scale.

As the project grows, there are too many things to remember:

- routes
- forms
- API responses
- case statuses
- validation rules
- authentication
- error pages

Tests give us a repeatable way to check expected behavior.

## Why This Matters for My Projects

### PHP Support Case System

Tests can protect:

- home route
- cases route
- 404 route
- case listing
- case lookup by ID
- future case creation

### Flask Blogging App

Tests can protect:

- API response shape
- database behavior
- endpoint contracts
- create/read/update/delete behavior

### prod-platform

Tests can protect:

- health endpoints
- service status responses
- monitoring logic
- failure detection

## AI Connection

AI can generate code quickly, but generated code is not automatically correct.

Tests define the expected behavior.

This means AI can help write or refactor code, but the tests decide whether the result is acceptable.

## Simple Testing Mindset

Before committing code, ask:

1. What behavior should work?
2. How can I prove it works?
3. Can I repeat that proof automatically?
4. Did the change break anything that worked before?

## Dojo Questions

1. What is a regression?
2. Why is manual checking not enough as a project grows?
3. What does a test protect?
4. In the PHP Support Case System, what route would be useful to test first?
5. Why are tests useful when AI writes or changes code?
6. What should happen before we commit code?
