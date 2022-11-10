import pytest

from src.viper_boot.enums.gender_enum import GenderEnum


@pytest.mark.parametrize(
    "cls",
    [GenderEnum],
    ids=[
        "it should contains '[`MALE`, `FEMALE`]' values",
    ]
)
def test_gender_enum(cls):
    for enum in cls:
        assert enum.name in ["MALE", "FEMALE"]
