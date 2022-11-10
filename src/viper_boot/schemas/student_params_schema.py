"""Student Params Schema."""
from marshmallow import fields
from marshmallow import Schema


class StudentParamsSchema(Schema):
    """
    Schema to represent Student parameters object.

    Properties:
        id (int): student id
    """

    id = fields.UUID(
        required=True,
        metadata={"description": "Student Id."},
    )
