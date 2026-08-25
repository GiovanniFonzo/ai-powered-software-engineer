from src.calculator import add, subtract


def test_user_calculator_journey():
    starting_value = 100

    value_after_deposit = add(starting_value, 50)
    final_value = subtract(value_after_deposit, 25)

    assert final_value == 125
