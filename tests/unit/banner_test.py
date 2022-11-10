import pytest

from src.viper_boot.utils.banner import Banner


@pytest.mark.parametrize(
    "cls",
    [Banner],
    ids=[
        "it should create instance of Banner",
    ]
)
def test__init__(cls):
    # Arrange, Act
    obj = cls()

    # Assert
    assert obj.__class__.__name__ == cls.__name__


@pytest.mark.parametrize(
    "cls",
    [Banner],
    ids=[
        "it should print banner in console",
    ]
)
def test_paste(cls, capfd):
    # Arrange, Act
    obj = cls()
    obj.paste()
    out, err = capfd.readouterr()

    # Assert
    assert err == capfd.captureclass.EMPTY_BUFFER
