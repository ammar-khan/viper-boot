import uuid

import pytest

from src.viper_boot.services.student_service import StudentService


@pytest.mark.parametrize(
    "cls",
    [StudentService],
    ids=[
        "it should create instance of StudentService.",
    ]
)
def test_student_service(cls):
    # Arrange, Act
    obj = cls()

    # Assert
    assert obj.__class__.__name__ == cls.__name__


@pytest.mark.parametrize(
    "cls",
    [StudentService],
    ids=[
        "it should return valid response.",
    ]
)
def test_get(cls, get_response):
    # Arrange
    _id = uuid.uuid4().hex

    # Act
    response = cls.get(_id)

    # Assert
    assert response["id"] != ""
    assert response["student"]["first_name"] != ""
    assert response["student"]["last_name"] != ""
    assert response["student"]["dob"] != ""
    assert response["student"]["gender"] != ""


@pytest.mark.parametrize(
    "cls",
    [StudentService],
    ids=[
        "it should return valid response.",
    ]
)
def test_get_all(cls, get_all_response):
    # Arrange
    _id = uuid.uuid4().hex

    # Act
    response = cls.get_all()

    # Assert
    assert response[0]["id"] != ""
    assert response[0]["student"]["first_name"] != ""
    assert response[0]["student"]["last_name"] != ""
    assert response[0]["student"]["dob"] != ""
    assert response[0]["student"]["gender"] != ""

    assert response[1]["id"] != ""
    assert response[1]["student"]["first_name"] != ""
    assert response[1]["student"]["last_name"] != ""
    assert response[1]["student"]["dob"] != ""
    assert response[1]["student"]["gender"] != ""


@pytest.mark.parametrize(
    "cls",
    [StudentService],
    ids=[
        "it should return valid response.",
    ]
)
def test_post(cls, post_request):
    # Arrange  Act
    response = cls.post(post_request)

    # Assert
    assert response["id"] != ""


@pytest.mark.parametrize(
    "cls",
    [StudentService],
    ids=[
        "it should return valid response.",
    ]
)
def test_patch(cls, patch_request):
    # Arrange
    _id = uuid.uuid4().hex

    # Act
    response = cls.patch(_id, patch_request)

    # Assert
    assert response["id"] != ""
    assert response["student"]["first_name"] != ""
    assert response["student"]["last_name"] != ""
    assert response["student"]["dob"] != ""
    assert response["student"]["gender"] != ""


@pytest.mark.parametrize(
    "cls",
    [StudentService],
    ids=[
        "it should return valid response.",
    ]
)
def test_delete(cls):
    # Arrange
    _id = uuid.uuid4().hex

    # Act
    response = cls.delete(_id)

    # Assert
    assert response != ""
