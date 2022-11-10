import pytest

from src.viper_boot.utils.decorators.singleton_decorator import (
    singleton
)


@pytest.mark.parametrize(
    "cls",
    [singleton],
    ids=[
        "it should return same instance of the class.",
    ]
)
def test_singleton(cls):
    # Arrange
    @singleton
    class SingletonClass:
        def __init__(self, arg: str = ""):
            self.arg = arg

    # Act
    object1 = SingletonClass("singleton")
    object2 = SingletonClass()

    # Assert
    assert object1.arg == object2.arg
