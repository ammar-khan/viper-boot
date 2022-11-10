import pytest

from src.viper_boot.schemas.student_id_schema import StudentIdSchema


@pytest.mark.parametrize(
    "cls",
    [StudentIdSchema],
    ids=[
        "it should create instance of StudentIdSchema.",
    ]
)
def test_student_id_schema(cls):
    # Arrange, Act
    obj = cls()

    # Assert
    assert obj.__class__.__name__ == cls.__name__


@pytest.mark.parametrize(
    "cls",
    [StudentIdSchema],
    ids=[
        "it should contain `id` attribute.",
    ]
)
def test_student_id_schema_id_attribute(cls):
    # Arrange, Act
    obj = cls()

    # Assert
    assert "id" in obj.__class__.__dict__["_declared_fields"]
