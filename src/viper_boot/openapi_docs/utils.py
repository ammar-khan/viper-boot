"""OpenAPI spec utilities."""
from string import Formatter
from typing import Any


def get_path_keys(path: str) -> Any:
    """
    Get keys from the path specified.

    Parameters:
        path (str): Path string

    Returns:
        keys in the path
    """
    return [i[1] for i in Formatter().parse(path) if i[1]]
