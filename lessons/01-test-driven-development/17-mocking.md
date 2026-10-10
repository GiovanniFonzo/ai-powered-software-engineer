# Step 17 — Mocking

## Main Idea

Mocking means replacing a real dependency with a fake version during a test.

Key memory:

    Mocking = fake external dependency for testing

A dependency can be something like:

    API call
    database
    email service
    payment service
    file system
    external website
    Salesforce connector

## Why Mocking Matters

Without mocking, tests can become:

    slow
    fragile
    expensive
    dependent on internet or service availability
    dangerous if they change real data

With mocking, we can test our own logic safely.

The goal is usually not to test whether the external service works.

The goal is to test whether our code behaves correctly when the external service returns a known response.

## Testing Our Code vs Testing an External Service

Testing our code means checking how our application behaves.

Testing an external service means checking whether another system works.

In our own test suite, we usually want to verify our logic, not Salesforce, Stripe, Gmail, or another third-party system.

## Practical Example

In this step, we created:

    src/tax_service.py
    tests/test_tax_service.py

The production function accepts a dependency:

    get_tax_rate

In the test, we provided a fake dependency:

    fake_get_tax_rate

The fake function returned:

    0.23

Then we tested that:

    calculate_total_with_tax(100, "IE", fake_get_tax_rate)

returned:

    123.0

The full test suite passed:

    14 passed

## Why This Helps with AI

When AI writes code that calls APIs or external systems, tests should not depend on the real external system.

Mocking lets us tell AI:

    assume the API returned this response
    now test how our code handles it

This makes the test faster, safer, and more predictable.

## Connection to PHP Support Case System and Salesforce

In the PHP Support Case System or a Salesforce connector, we could mock:

    successful API responses
    invalid_grant errors
    timeout errors
    500 errors
    database responses
    failed connector responses

This would let us test error handling safely without calling the real Salesforce API.

## Dojo Answers

1. Mocking in testing means replacing a real dependency with a fake version during a test.

2. Mocking is useful because it lets us test our own logic safely without depending on real external systems.

3. Things that can be mocked include API calls, databases, email services, payment services, the file system, external websites, and Salesforce connectors.

4. Tests should avoid depending on real external APIs because they can be slow, fragile, expensive, unavailable, and dangerous if they change real data.

5. Testing our code means checking how our application behaves. Testing an external service means checking whether another system works. In our tests, we usually want to verify our own logic, not Salesforce, Stripe, Gmail, or another third-party service.

6. In the calculator project, we do not really need mocking yet because add(), subtract(), and multiply() do not depend on external systems. They only calculate values directly.

7. In the PHP Support Case System or Salesforce connector example, we could mock API calls, database responses, successful Salesforce responses, invalid_grant errors, timeout errors, 500 errors, or failed connector responses.
