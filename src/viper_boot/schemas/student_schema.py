"""Student Schema."""
from marshmallow import fields
from marshmallow import INCLUDE
from marshmallow import Schema

from .person_schema import PersonSchema


class StudentSchema(Schema):
    """
    Schema to represent Student object.

    Properties:
        id (int): student id
        student (PersonSchema): student object
    """

    class Meta:
        """Configure schema meta for Student Schema."""

        unknown = INCLUDE  # pylint: disable=R0801

    id = fields.UUID(
        dump_only=True,
        metadata={"description": "Student Id."},
    )
    student = fields.Nested(
        PersonSchema(),
        metadata={
            "description": "Student object."
        },
    )
