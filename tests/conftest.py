import uuid
from datetime import datetime

import pytest

from src.viper_boot.enums import GenderEnum


@pytest.fixture
def get_response():
    data = {
        "id": uuid.uuid4().hex,
        "student": {
            "first_name": "James",
            "last_name": "Smith",
            "dob": datetime.strptime("10/10/1978", "%d/%m/%Y").date(),
            "gender": GenderEnum.MALE,
        },
    }

    return data


@pytest.fixture
def get_all_response(get_response):
    data = [
        get_response,
        get_response
    ]

    return data


@pytest.fixture
def post_request():
    data = {
        "first_name": "James",
        "last_name": "Smith",
        "dob": datetime.strptime("10/10/1978", "%d/%m/%Y").date(),
        "gender": GenderEnum.MALE,
    }

    return data


@pytest.fixture
def patch_request(post_request):
    data = {
        "first_name": "James",
        "last_name": "Smith",
        "dob": datetime.strptime("10/10/1978", "%d/%m/%Y").date().isoformat(),
        "gender": GenderEnum.MALE.name,
    }

    return data


@pytest.fixture
def patch_response(get_response):
    data = get_response

    return data
