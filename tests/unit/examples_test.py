import pytest

from src.viper_boot.examples.python import add_number
from src.viper_boot.examples.python import InvalidIntegerError


@pytest.mark.parametrize(
    "operand_one, operand_two, expected",
    [(1, 1, 2), (2, 2, 4), (3, 6, 9), (10, 3628800, 3628810)],
    ids=[
        "it should return `2` when operand_one is `1` and operand_two is `1`.",  # noqa
        "it should return `4` when operand_one is `2` and operand_two is `2`.",  # noqa
        "it should return `9` when operand_one is `3` and operand_two is `6`.",  # noqa
        "it should return `3628810` when operand_one is `10` and operand_two is `3628800`.",  # noqa
    ]
)
def test_add_number(operand_one: int, operand_two: int, expected: int) -> None:
    # Arrange, Act, Assert
    assert add_number(operand_one, operand_two) == expected


@pytest.mark.parametrize(
    "operand_one, operand_two",
    [(-1, 1), (2, -2)],
    ids=[
        "it should raise InvalidIntegerError exception when operand_one is `-1` and operand_two is `1`.",  # noqa
        "it should raise InvalidIntegerError exception when operand_one is `2` and operand_two is `-2`.",  # noqa
    ]
)
def test_invalid_add_number(operand_one: int, operand_two: int) -> None:
    # Arrange, Act, Assert
    with pytest.raises(InvalidIntegerError):
        add_number(operand_one, operand_two)
