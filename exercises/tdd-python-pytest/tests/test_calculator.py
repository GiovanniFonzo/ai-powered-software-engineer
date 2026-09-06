import pytest

from src.calculator import add, subtract, multiply


@pytest.fixture
def positive_numbers():
    return 3, 4


@pytest.mark.parametrize(
    "first_number, second_number, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (10, 0, 10),
        (3, 4, 7),
    ],
)
def test_add_returns_expected_sum(first_number, second_number, expected):
    result = add(first_number, second_number)

    assert result == expected


@pytest.mark.parametrize(
    "first_number, second_number, expected",
    [
        (10, 4, 6),
        (-10, -4, -6),
        (10, 10, 0),
    ],
)
def test_subtract_returns_expected_difference(first_number, second_number, expected):
    result = subtract(first_number, second_number)

    assert result == expected


@pytest.mark.parametrize(
    "first_number, second_number, expected",
    [
        (3, 4, 12),
        (10, 0, 0),
        (-2, 3, -6),
    ],
)
def test_multiply_returns_expected_product(first_number, second_number, expected):
    result = multiply(first_number, second_number)

    assert result == expected


def test_multiply_returns_product_of_positive_numbers_from_fixture(positive_numbers):
    first_number, second_number = positive_numbers

    result = multiply(first_number, second_number)

    assert result == 12


