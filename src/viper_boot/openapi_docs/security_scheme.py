"""Authentication Scheme."""
from typing import Dict

from ..utils.decorators.singleton_decorator import singleton


class _SecurityScheme:
    """
    API authentication scheme base class.

    Attribute:
        _security_header (str): security header string for API
    """

    def __init__(self) -> None:
        """Set security scheme for API."""
        self._security_header: Dict[str, str] = {}


@singleton
class _ApiKey(_SecurityScheme):
    """
    Security scheme for API Key.

    Constants:
        _DEFAULT_AUTH_HEADER (str): default API Key header
    """

    _DEFAULT_AUTH_HEADER: str = "X-API-Key"

    def __init__(self, auth_header: str = "") -> None:
        """
        Set authentication scheme for API Key.

        Parameters:
            auth_header (str): header name for authentication

        """
        super().__init__()
        self.auth_header = auth_header or self._DEFAULT_AUTH_HEADER

    @property
    def security_header(self) -> Dict[str, str]:
        """
        Getter method for authentication header.

        Returns:
            authentication header json object
        """
        self._security_header = {
            "type": "apiKey",
            "in": "header",
            "name": self.auth_header,
        }

        return self._security_header


@singleton
class _Jwt(_SecurityScheme):
    """API authentication scheme for JSON Web Token."""

    def __init__(self) -> None:  # pylint: disable=useless-parent-delegation
        """Set authentication scheme for JWT."""
        super().__init__()

    @property
    def security_header(self) -> Dict[str, str]:
        """
        Getter method for authentication header.

        Returns:
            authentication header json object
        """
        self._security_header = {
            "type": "http",
            "bearerFormat": "JWT",
            "scheme": "bearer",
        }

        return self._security_header


apikey_header = _ApiKey()
jwt_header = _Jwt()
