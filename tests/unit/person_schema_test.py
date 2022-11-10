import pytest

from src.viper_boot.schemas.person_schema import (
    PersonSchema
)


@pytest.mark.parametrize(
    "cls",
    [PersonSchema],
    ids=[
        "it should create instance of StudentIdSchema.",
    ]
)
def test_person_schema(cls):
    # Arrange, Act
    obj = cls()

    # Assert
    assert obj.__class__.__name__ == cls.__name__


@pytest.mark.parametrize(
    "cls",
    [PersonSchema],
    ids=[
        "it should contain `first_name` attribute.",
    ]
)
def test_person_schema_id_attribute(cls):
    # Arrange, Act
    obj = cls()

    # Assert
    assert "first_name" in obj.__class__.__dict__["_declared_fields"]
