"""Student Id Schema."""
from marshmallow import fields
from marshmallow import INCLUDE
from marshmallow import Schema


class StudentIdSchema(Schema):
    """
    Schema to represent Student id object.

    Properties:
        id (int): student id
    """

    class Meta:
        """Configure schema meta for StudentIdSchema."""

        unknown = INCLUDE  # pylint: disable=R0801

    id = fields.UUID(
        dump_only=True,
        metadata={
            "description": "Student Id."
        },
    )
