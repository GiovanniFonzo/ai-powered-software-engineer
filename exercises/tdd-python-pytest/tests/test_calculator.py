from src.calculator import add, subtract, multiply


def test_add_returns_sum_of_two_positive_numbers():
    result = add(2, 3)

    assert result == 5


def test_add_returns_sum_of_two_negative_numbers():
    result = add(-2, -3)

    assert result == -5


def test_add_returns_same_number_when_adding_zero():
    result = add(10, 0)

    assert result == 10


def test_subtract_returns_difference_of_two_positive_numbers():
    result = subtract(10, 4)

    assert result == 6


def test_subtract_returns_difference_of_two_negative_numbers():
    result = subtract(-10, -4)

    assert result == -6


def test_subtract_returns_zero_when_numbers_are_equal():
    result = subtract(10, 10)

    assert result == 0


def test_multiply_returns_product_of_two_positive_numbers():
    result = multiply(3, 4)

    assert result == 12


def test_multiply_returns_zero_when_multiplying_by_zero():
    result = multiply(10, 0)

    assert result == 0

