import pytest

from src.viper_boot.models.student_model import StudentModel


@pytest.mark.parametrize(
    "cls",
    [StudentModel],
    ids=[
        "it should create instance of StudentModel",
    ]
)
def test_student_model(cls):
    # Arrange, Act
    obj = cls()

    # Assert
    assert obj.__class__.__name__ == cls.__name__
