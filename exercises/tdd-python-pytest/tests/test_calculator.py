from src.calculator import add, subtract


def test_add_two_positive_numbers():
    result = add(2, 3)

    assert result == 5


def test_add_two_negative_numbers():
    result = add(-2, -3)

    assert result == -5


def test_add_zero_to_number():
    result = add(10, 0)

    assert result == 10


def test_subtract_two_positive_numbers():
    result = subtract(10, 4)

    assert result == 6


def test_subtract_two_negative_numbers():
    result = subtract(-10, -4)

    assert result == -6


def test_subtract_to_zero():
    result = subtract(10, 10)

    assert result == 0

