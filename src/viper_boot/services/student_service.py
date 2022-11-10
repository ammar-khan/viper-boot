"""Student Service."""
import uuid
from datetime import datetime
from typing import Any
from typing import Dict

import requests

from ..config.config import Config
from ..enums.gender_enum import GenderEnum
from ..schemas import StudentIdSchema
from ..schemas import StudentSchema

SETTINGS = Config().get


class StudentService:
    """Service for student controller."""

    def __init__(self) -> None:
        """Service constructor."""
        pass  # pylint: disable=unnecessary-pass

    @staticmethod
    def get(_id: str = None) -> Any:
        """
        Get student by id.

        Parameters:
            _id (str) : student id

        Returns:
            (Any): student
        """
        # Get API link from settings
        api_uri = SETTINGS["API"]["url"]

        # Make API call
        response = requests.get(api_uri, timeout=(3.05, 27))
        response.raise_for_status()

        data = {
            "id": uuid.uuid4().hex,
            "student": {
                "first_name": "James",
                "last_name": "Smith",
                "dob": datetime.strptime("10/10/1978", "%d/%m/%Y").date().isoformat(),  # noqa  # pylint: disable=line-too-long
                "gender": GenderEnum.MALE.name,
            },
        }

        # Deserializing Object
        return StudentSchema().load(data)

    @staticmethod
    def get_all() -> Any:
        """
        Get all students.

        Returns:
            (Any): list of all students  # type: ignore
        """
        # Get API link from settings
        api_uri = SETTINGS["API"]["url"]

        # Make API call
        response = requests.get(api_uri, timeout=(3.05, 27))
        response.raise_for_status()

        data = [
            {
                "id": uuid.uuid4().hex,
                "student": {
                    "first_name": "James",
                    "last_name": "Smith",
                    "dob": datetime.strptime("10/10/1978", "%d/%m/%Y").date().isoformat(),  # noqa  # pylint: disable=line-too-long
                    "gender": GenderEnum.MALE.name,
                },
            },
            {
                "id": uuid.uuid4().hex,
                "student": {
                    "first_name": "Sarah",
                    "last_name": "Smith",
                    "dob": datetime.strptime("10/10/1988", "%d/%m/%Y").date().isoformat(),  # noqa  # pylint: disable=line-too-long
                    "gender": GenderEnum.FEMALE.name,
                },
            },
        ]

        # Deserializing Object
        return StudentSchema(many=True).load(data)

    @staticmethod
    def post(request: Any) -> Any:  # pylint: disable=unused-argument
        """
        Create new student.

        Parameters:
            request (Any) : student request object

        Returns:
            student id
        """
        # Get API link from settings
        api_uri = SETTINGS["API"]["url"]

        # Make API call
        response = requests.get(api_uri, timeout=(3.05, 27))
        response.raise_for_status()

        data = {"id": uuid.uuid4().hex}

        # Deserializing Object
        return StudentIdSchema().load(data)

    @staticmethod
    def patch(_id: str, request: Any) -> Any:
        """
        Update student.

        Parameters:
            _id (str): student id
            request (Any): student request object

        Returns:
            schema (Any): student response object
        """
        # Get API link from settings
        api_uri = SETTINGS["API"]["url"]

        # Make API call
        response = requests.get(api_uri, timeout=(3.05, 27))
        response.raise_for_status()

        data = {
            "id": _id,
            "student": request,
        }

        # Deserializing Object
        return StudentSchema().load(data)

    @staticmethod
    def delete(_id: str) -> Any:
        """
        Delete student by id.

        Parameters:
            _id (str) : student id

        Returns:
            data(Dict[str, Any]): exception if fail
        """
        # Get API link from settings
        api_uri = SETTINGS["API"]["url"]

        # Make API call
        response = requests.get(api_uri, timeout=(3.05, 27))
        response.raise_for_status()

        # Return exception if fail
        data: Dict[str, Any] = {}

        return data
