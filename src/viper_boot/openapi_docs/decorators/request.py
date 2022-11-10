"""Open Api Specs request decorator."""
import copy
from functools import partial
from typing import Any


# locations supported by openapi
VALID_SCHEMA_LOCATIONS = (
    "cookies",
    "files",
    "form",
    "headers",
    "json",
    "match_info",
    "path",
    "query",
    "querystring",
)


def request_schema(
    schema: Any,
    location: str = "json",
    put_into: Any = None,
    example: Any = None,
    add_to_refs: bool = False,
    **kwargs: Any,
) -> Any:
    """Request info for Open API docs.

    Add request info into the swagger spec.
    put_into (Any): name of the key in Request object where validated
    data will be placed. If None (by default) default key will be used

    add_to_refs (bool): Working only if example not None, if True,
    add example for ref schema, otherwise add example to endpoint.

    Parameters:
        schema (Any): `Schema <marshmallow.Schema>` class or instance
        location (str): Default request locations to parse
        put_into (Any): name of the key in Request object
        example (Any): Adding example for current schema
        add_to_refs (bool): Default False
        **kwargs (Any): extra arguments

    Raises:
        ValueError: if invalid location found or if multiple location found

    Returns:
        function of annotation
    """  # noqa: RST210
    if location not in VALID_SCHEMA_LOCATIONS:
        raise ValueError(f"Invalid location argument: {location}")

    if callable(schema):
        schema = schema()

    options = {"required": kwargs.pop("required", False)}

    def wrapper(func: Any) -> Any:
        if not hasattr(func, "__apispec__"):
            func.__apispec__ = {
                "schemas": [],
                "responses": {},
                "parameters": [],
            }
            func.__schemas__ = []

        _example = copy.copy(example) or {}
        if _example:
            _example["add_to_refs"] = add_to_refs
        func.__apispec__["schemas"].append(
            {
                "schema": schema,
                "location": location,
                "options": options,
                "example": _example,
            }
        )

        # "body" location was replaced by "json" location
        if location == "json" and any(
            func_schema["location"] == "json"
            for func_schema in func.__schemas__
        ):
            raise RuntimeError("Multiple json locations are not allowed")

        func.__schemas__.append(
            {"schema": schema, "location": location, "put_into": put_into}
        )

        return func

    return wrapper


# For backward compatibility
use_kwargs = request_schema

# Decorators for specific request data validations (shortenings)
match_info_schema = partial(
    request_schema, location="match_info", put_into="match_info"
)
querystring_schema = partial(
    request_schema, location="querystring", put_into="querystring"
)
form_schema = partial(request_schema, location="form", put_into="form")
json_schema = partial(request_schema, location="json", put_into="json")
headers_schema = partial(
    request_schema, location="headers", put_into="headers"
)
cookies_schema = partial(
    request_schema, location="cookies", put_into="cookies"
)
