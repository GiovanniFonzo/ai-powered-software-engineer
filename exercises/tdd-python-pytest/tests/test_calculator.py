from src.calculator import add


def test_add_two_numbers():
    result = add(2, 3)

    assert result == 5
