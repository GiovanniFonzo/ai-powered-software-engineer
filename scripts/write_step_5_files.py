from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

lesson = """# Step 5: Motivation for Test-Driven Development

## Main Idea

The main motivation for Test-Driven Development is to define what working means before writing the code.

Instead of waiting until the end to check manually, we write a test first.

The test describes the expected behavior.

## Normal Workflow

Without TDD, the workflow is often:

    Write code -> manually check -> fix bugs later

This can work for very small examples, but it becomes risky as a project grows.

## TDD Workflow

With TDD, the workflow is:

    Write test -> watch it fail -> write code -> pass test -> refactor

This is called:

    Red -> Green -> Refactor

## Why Write the Test First?

Writing the test first gives clarity before coding.

The test acts like a small contract.

Example:

    subtract(10, 4) should return 6

That expected behavior becomes the test.

## Practical Example

We added this test first:

    def test_subtract_two_numbers():
        result = subtract(10, 4)

        assert result == 6

When we ran pytest, it failed with:

    ImportError: cannot import name 'subtract'

This happened because the test expected a subtract function, but the function did not exist yet.

That was the Red step.

Then we added the function:

    def subtract(first_number, second_number):
        return first_number - second_number

After running pytest again, the result was:

    2 passed

That was the Green step.

## Why This Matters

TDD helps because:

- it clarifies the requirement before coding
- it catches missing behavior early
- it reduces fear when refactoring
- it protects expected behavior
- it gives AI-generated code a clear target

## AI Connection

TDD is especially useful with AI-generated code.

Instead of asking AI to write code that only looks correct, we can define tests first.

Then AI must produce code that satisfies those tests.

The tests become the standard for whether the generated code is acceptable.

## PHP Support Case System Connection

Before building /cases/create, we could define tests for:

- valid case creation
- missing required fields
- invalid data handling
- unknown case IDs
- correct redirect or response after creation

This means we define expected behavior before writing the implementation.

## Dojo Answers

1. The main motivation for TDD is to define what working means before writing the code, instead of waiting until the end to check manually.

2. We write the test before the code because it gives us clarity before coding. The test defines the expected behavior first.

3. The test acts like a contract. It describes the behavior the code must satisfy.

4. TDD reduces fear when refactoring because if the tests still pass, we know the expected behavior is protected.

5. TDD helps with AI-generated code because we can give AI the tests first. Then AI must write code that satisfies those tests instead of only producing code that looks correct.

6. Before building /cases/create in the PHP Support Case System, we could define tests for valid case creation, missing required fields, and invalid data handling.
"""

path = ROOT / "lessons/01-test-driven-development/05-motivation-for-tdd.md"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(lesson, encoding="utf-8")

print(f"Wrote {path}")
