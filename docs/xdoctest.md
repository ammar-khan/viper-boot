# Xdoctest

## Usage

```python
def add_number(operand_one: int, operand_two: int) -> int:
    """
    Accept two integer values and sum them up and return the sum.

    Example:
        >>> add_number(5 + 5)  # xdoctest: +SKIP
        10

        >>> add_number(1 + 1)  # xdoctest: +SKIP
        2

        >>> add_number(-1 + 2)  # xdoctest: +SKIP
        InvalidIntegerError

    Parameters:
        operand_one (int): first number
        operand_two (int): second number

    Raises:
        InvalidIntegerError: If operand_one or operand_two is less than 0.

    Returns:
        Sum of two numbers
    """
    if operand_one < 0 or operand_two < 0:
        raise InvalidIntegerError(
            f"""operand_one or operand_two is less than zero:
            operand_one={operand_one}, operand_two={operand_two}"""
        )

    add: int = operand_one + operand_two
    return add
```

!!! note

    3 tests are writted in docstring which will be executed by xdoctest

    ```python
    Example:
        >>> add_number(5 + 5)  # xdoctest: +SKIP
        10

        >>> add_number(1 + 1)  # xdoctest: +SKIP
        2

        >>> add_number(-1 + 2)  # xdoctest: +SKIP
        InvalidIntegerError
    ```
```python
>>> add_number(5 + 5)  # xdoctest: +SKIP
10 # (1)
```


1. This assertion will be `True`

Please see the [readthedocs](https://xdoctest.readthedocs.io/) for details.
