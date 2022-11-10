import uuid

import pytest

from src.viper_boot.controllers.student_controller import (
    StudentController
)


@pytest.mark.parametrize(
    "cls",
    [StudentController],
    ids=[
        "it should create instance of StudentController.",
    ]
)
def test_student_controller(cls):
    # Arrange, Act
    obj = cls()

    # Assert
    assert obj.__class__.__name__ == cls.__name__


@pytest.mark.parametrize(
    "cls",
    [StudentController],
    ids=[
        "it should return list of schema.",
    ]
)
def test_schema(cls):
    # Arrange
    obj = cls()

    # Act, Assert
    assert obj.schemas is not None


@pytest.mark.parametrize(
    "cls",
    [StudentController],
    ids=[
        "it should call StudentService.get.",
    ]
)
def test_get(cls, get_response, mocker):
    # Arrange
    _id = uuid.uuid4().hex
    spy = mocker.patch(
        "src.viper_boot.services.StudentService.get",
        return_value=get_response
    )

    # Act
    response = cls.get(_id)

    # Assert
    spy.assert_called_once_with(_id)

    assert response["id"] != ""
    assert response["student"]["first_name"] != ""
    assert response["student"]["last_name"] != ""
    assert response["student"]["dob"] != ""
    assert response["student"]["gender"] != ""


@pytest.mark.parametrize(
    "cls",
    [StudentController],
    ids=[
        "it should call StudentService.get_all.",
    ]
)
def test_get_all(cls, get_all_response, mocker):
    # Arrange
    _id = uuid.uuid4().hex
    spy = mocker.patch(
        "src.viper_boot.services.StudentService.get_all",
        return_value=get_all_response
    )

    # Act
    response = cls.get_all()

    # Assert
    spy.assert_called_once_with()

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
    [StudentController],
    ids=[
        "it should call StudentService.post.",
    ]
)
def test_post(cls, post_request, mocker):
    # Arrange
    spy = mocker.patch(
        "src.viper_boot.services.StudentService.post",
        return_value={"id": uuid.uuid4().hex}
    )

    # Act
    response = cls.post(post_request)

    # Assert
    spy.assert_called()

    assert response["id"] != ""


@pytest.mark.parametrize(
    "cls",
    [StudentController],
    ids=[
        "it should call StudentService.patch.",
    ]
)
def test_patch(cls, patch_request, get_response, mocker):
    # Arrange
    _id = uuid.uuid4().hex
    spy = mocker.patch(
        "src.viper_boot.services.StudentService.patch",
        return_value=get_response
    )

    # Act
    response = cls.patch(_id, patch_request)

    # Assert
    spy.assert_called()

    assert response["id"] != ""
    assert response["student"]["first_name"] != ""
    assert response["student"]["last_name"] != ""
    assert response["student"]["dob"] != ""
    assert response["student"]["gender"] != ""


@pytest.mark.parametrize(
    "cls",
    [StudentController],
    ids=[
        "it should call StudentService.delete.",
    ]
)
def test_delete(cls, mocker):
    # Arrange
    _id = uuid.uuid4().hex
    spy = mocker.patch(
        "src.viper_boot.services.StudentService.delete",
        return_value={}
    )

    # Act
    response = cls.delete(_id)

    # Assert
    spy.assert_called()

    assert response != ""
