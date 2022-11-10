"""Person Schema."""
from datetime import datetime

from marshmallow import fields
from marshmallow import Schema


class PersonSchema(Schema):
    """
    Schema to represent Person object.

    Properties:
        first_name (str): first name
        last_name (str): last name
        dob (date): date of birth
        gender (str): gender
    """

    first_name = fields.Str(
        required=True, metadata={"description": "First name"}
    )
    last_name = fields.Str(
        required=True, metadata={"description": "Last name"}
    )
    dob = fields.Date(
        required=True,
        dump_default=datetime.today(),
        metadata={
            "description": "Date of birth",
            "default": "Today date",
        },
    )
    gender = fields.String(
        required=True,
        metadata={
            "description": "Gender",
            "enum": ["MALE", "FEMALE"],
        },
    )
