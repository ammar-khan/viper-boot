"""Student Controller."""
from typing import Any

from ..schemas import PersonSchema
from ..schemas import StudentIdSchema
from ..schemas import StudentParamsSchema
from ..schemas import StudentSchema
from ..services import StudentService


class StudentController:
    """API controller for student."""

    def __init__(self) -> None:
        """Initialise the controller."""
        self._schemas = (
            PersonSchema,
            StudentSchema,
            StudentIdSchema,
            StudentParamsSchema,
        )

    @staticmethod
    def get(_id: str = None) -> Any:
        """
        Endpoint handler for get API, returns all students.

        Parameters:
            _id (str) : student id

        Returns:
            (StudentSchema): API response
        """
        # Serializing Object
        return StudentSchema().dump(StudentService.get(_id))

    @staticmethod
    def get_all() -> Any:
        """
        Endpoint handler for get API, returns all students.

        Returns:
            (StudentSchema): API response
        """
        # Serializing Object
        return StudentSchema(many=True).dump(StudentService.get_all())

    @staticmethod
    def post(request: PersonSchema) -> Any:
        """
        Endpoint handler for post API, create student.

        Parameters:
            request (PersonSchema) : student request object

        Returns:
            (StudentIdSchema): API response
        """
        # Serializing Object
        return StudentService.post(PersonSchema().dump(request))

    @staticmethod
    def patch(_id: str, request: PersonSchema) -> Any:
        """
        Endpoint handler for get API, returns all students.

        Parameters:
            _id (str): student id
            request (PersonSchema): student object

        Returns:
            (StudentSchema): API response
        """
        # Serializing Object
        return StudentSchema().dump(StudentService.patch(_id, request))

    @staticmethod
    def delete(_id: str = None) -> Any:
        """
        Endpoint handler for delete API, returns exception if fail.

        Parameters:
            _id (str) : student id

        Returns:
            Error if fail
        """
        return StudentService.delete(_id)

    @property
    def schemas(self) -> Any:
        """
        Getter for response schemas of API.

        Returns:
            response schemas
        """
        return self._schemas
