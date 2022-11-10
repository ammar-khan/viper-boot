"""Open Api Specs response decorator."""
from typing import Any


def response_schema(
    schema: Any,
    code: int = 200,
    required: bool = False,
    description: str = "",
) -> Any:
    """Add response info into the swagger spec.

    Parameters:
        description (str): response description
        required (bool): required or not
        schema: (Any): `Schema <marshmallow.Schema>` class or instance
        code (int): HTTP response code

    Returns:
        function of annotation
    """  # noqa: DAR002
    if callable(schema):
        schema = schema()

    def wrapper(func: Any) -> Any:
        if not hasattr(func, "__apispec__"):
            func.__apispec__ = {
                "schemas": [],
                "responses": {},
                "parameters": [],
            }
            func.__schemas__ = []
        func.__apispec__["responses"][f"{code}"] = {
            "schema": schema,
            "required": required,
            "description": description or "",
        }
        return func

    return wrapper


# For backward compatibility
marshal_with = response_schema
