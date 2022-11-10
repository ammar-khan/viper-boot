"""Main Application Handler."""
import json
import webbrowser
from typing import Any

import click

from .config.config import Config
from .controllers.student_controller import StudentController
from .openapi_docs.decorators import openapi
from .openapi_docs.decorators import response_schema
from .openapi_docs.open_api import OpenApi
from .utils.banner import Banner
from .utils.decorators import singleton


# Include all controllers
student_controller = StudentController()
(
    PersonSchema,
    StudentSchema,
    StudentIdSchema,
    StudentParamsSchema,
) = student_controller.schemas


@singleton
class _Application:
    """Main application class runner."""

    _openapi: Any

    def __init__(self) -> None:
        """Application Runner."""
        # Set application config environment
        Config().environment = "development"

        # Print project banner
        Banner.paste()

        # Register APIs with OpenAPI spec
        self._openapi = OpenApi()
        self._openapi.register("/api/v1/students", self.get_students)
        self._openapi.register("/api/v1/student/{id}", self.get_student_by_id)
        self._openapi.register("/api/v1/student", self.create_student)
        self._openapi.register("/api/v1/student/{id}", self.update_student)
        self._openapi.register("/api/v1/student/{id}", self.delete_student)

    @property
    def settings(self) -> str:
        """
        Getter method for application settings.

        Returns:
            Application settings
        """
        return self.settings

    def openapi_serve(self) -> None:
        """Serve OpenAPI docs."""
        # Generate Open API docs
        self._openapi.generate_doc()

        # Serve Open API docs
        webbrowser.open("http://127.0.0.1:3000", new=2)
        self._openapi.serve_doc()

    # Get all students API
    # path="/api/v1/students"
    # --------------------
    @openapi(
        tags=["Student"],
        method="GET",
        summary="Get all students",
        description="Get all student from database",
        responses={
            200: {
                "description": "Ok. Get students",
                "content": {
                    "application/json": {
                        "schema": {"type": "array", "items": StudentSchema}
                    }
                },
                "links": {
                    "GetStudentById": {
                        "operationRef": "/api/student/{id}",
                        "parameters": {"id": "$response.body#/id"},
                        "description": "The `id` value returned in the "
                        "response can be used as "
                        "the `id` parameter "
                        "in `GET /api/student/{id}`.",
                    }
                },
            },
            400: {"description": "Bad request"},
            401: {"description": "Unauthorized"},
            422: {"description": "Validation error"},
            500: {"description": "Server error"},
        },
    )  # type: ignore
    @response_schema(StudentSchema)  # type: ignore
    def get_students(self) -> None:
        """Endpoint handler for student API, return all students."""
        response = student_controller.get_all()
        print(json.dumps(response, indent=2))

    # Get student by id API
    # path="/api/v1/student/{id}"
    # ---------------------
    @openapi(
        tags=["Student"],
        method="GET",
        summary="Get student by id",
        description="Get student by id from database",
        parameters=[
            {
                "in": "path",
                "name": "id",
                "schema": StudentParamsSchema,
                "required": "true",
            }
        ],
        responses={
            200: {
                "description": "Ok. Get student",
                "content": {"application/json": {"schema": StudentSchema}},
            },
            400: {"description": "Bad request"},
            401: {"description": "Unauthorized"},
            422: {"description": "Validation error"},
            500: {"description": "Server error"},
        },
    )  # type: ignore
    @response_schema(StudentSchema)  # type: ignore
    def get_student_by_id(self, _id: str) -> None:
        """
        Endpoint handler for student API, return particular students.

        Parameters:
            _id (str): student id
        """
        response = student_controller.get()
        print(json.dumps(response, indent=2))

    # Create student API
    # path="/api/v1/student"
    # ------------------
    @openapi(
        tags=["Student"],
        method="POST",
        summary="Create student",
        description="Create new student in database",
        requestBody={
            "description": "Optional description in *Markdown*",
            "required": True,
            "content": {"application/json": {"schema": PersonSchema}},
        },
        responses={
            201: {
                "description": "Ok. Create student",
                "content": {"application/json": {"schema": StudentIdSchema}},
            },
            400: {"description": "Bad request"},
            401: {"description": "Unauthorized"},
            422: {"description": "Validation error"},
            500: {"description": "Server error"},
        },
    )  # type: ignore
    # For OpenAPI >=3 we don"t need request_schema
    # @request_schema(PersonSchema)  # type: ignore
    def create_student(self, request: Any) -> None:
        """
        Endpoint handler for student API, create student.

        Parameters:
            request (Any): student request object
        """
        response = student_controller.post(request)
        print(json.dumps(response, indent=2))

    # Put student by id API
    # path="/api/v1/student/{id}"
    # ---------------------
    @openapi(
        tags=["Student"],
        method="PATCH",
        summary="Update student by id",
        description="Update student by id in database",
        parameters=[
            {
                "in": "path",
                "name": "id",
                "schema": StudentParamsSchema,
                "required": "true",
            }
        ],
        responses={
            200: {
                "description": "Ok. Student updated",
                "content": {"application/json": {"schema": StudentSchema}},
            },
            400: {"description": "Bad request"},
            401: {"description": "Unauthorized"},
            422: {"description": "Validation error"},
            500: {"description": "Server error"},
        },
    )  # type: ignore
    @response_schema(StudentSchema)  # type: ignore
    def update_student(self, _id: str, request: Any) -> None:
        """
        Endpoint handler for student API, update particular students.

        Parameters:
            _id (str): student id
            request (Any): student object
        """
        response = student_controller.patch(_id, request)
        print(json.dumps(response, indent=2))

    # Delete student by id API
    # path="/api/v1/student/{id}"
    # ---------------------
    @openapi(
        tags=["Student"],
        method="DELETE",
        summary="Delete student by id",
        description="Delete student by id from database",
        parameters=[
            {
                "in": "path",
                "name": "id",
                "schema": StudentParamsSchema,
                "required": "true",
            }
        ],
        responses={
            204: {"description": "Ok. Student deleted"},
            400: {"description": "Bad request"},
            401: {"description": "Unauthorized"},
            422: {"description": "Validation error"},
            500: {"description": "Server error"},
        },
    )  # type: ignore
    def delete_student(self, _id: str) -> None:
        """
        Endpoint handler for student API, delete particular students.

        Parameters:
            _id (str): student id
        """
        response = student_controller.delete(_id)
        print(json.dumps(response, indent=2))


@click.command()
@click.version_option()
def main() -> None:
    """viper_boot."""
    _Application()

    # Initialise, register and serve OpenAPI docs.
    _Application().openapi_serve()

    # Invoking APIs manually
    # _Application().get_student_by_id(uuid.uuid4().hex)
    # _Application().get_students()
    # _Application().create_student(
    #     {
    #         "first_name": "James",
    #         "last_name": "Smith",
    #         "dob": datetime(1978, 10, 10),
    #         "gender": GenderEnum.MALE,
    #     }
    # )
    # _Application().update_student(
    #     uuid.uuid4().hex,
    #     {
    #         "first_name": "James",
    #         "last_name": "Smith",
    #         "dob": datetime(1978, 10, 10).date().isoformat(),
    #         "gender": GenderEnum.MALE.name,
    #     }
    # )
    # _Application().delete_student(uuid.uuid4().hex)


if __name__ == "__main__":
    main(prog_name="viper_boot")  # pragma: no cover
