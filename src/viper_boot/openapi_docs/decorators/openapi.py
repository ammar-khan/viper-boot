"""Open Api Specs decorator."""
from typing import Any


def openapi(**kwargs: Any) -> Any:
    """Add docs info into the openapi spec.

    Parameters:
        **kwargs (Any): arguments

    Returns:
        function of annotation
    """  # noqa: RST210
    def wrapper(func: Any) -> Any:
        # Does not require by Open API Sec >=3.0
        # if not kwargs.get("produces"):
        #    kwargs["produces"] = ["application/json"]
        if not hasattr(func, "__apispec__"):
            func.__apispec__ = {
                "schemas": [],
                "responses": {},
                "parameters": [],
            }
            func.__schemas__ = []
        extra_parameters = kwargs.pop("parameters", [])
        extra_responses = kwargs.pop("responses", {})
        func.__apispec__["parameters"].extend(extra_parameters)
        func.__apispec__["responses"].update(extra_responses)
        func.__apispec__.update(kwargs)

        return func

    return wrapper
