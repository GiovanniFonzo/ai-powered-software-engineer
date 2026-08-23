from src.calculator import add, subtract


def test_calculator_workflow_add_then_subtract():
    starting_value = 10

    after_addition = add(starting_value, 5)
    final_result = subtract(after_addition, 3)

    assert final_result == 12
