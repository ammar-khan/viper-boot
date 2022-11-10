"""Singleton Class Decorator."""
from functools import wraps
from typing import Any
from typing import Callable
from typing import Dict
from typing import Tuple


def singleton(cls: Callable[..., Any]) -> Callable[..., Any]:
    """
    Singleton Class Decorator.

    Parameters:
        cls (class): class object

    Returns:
        Class object
    """
    instances = {}

    @wraps(cls)
    def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
