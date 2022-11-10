"""Open Api Specs."""
import copy
import json
import os
import subprocess
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from pathlib import Path
from typing import Any
from typing import Dict

import yaml
from apispec import APISpec
from apispec.core import VALID_METHODS_OPENAPI_V2
from apispec.ext.marshmallow import common
from apispec.ext.marshmallow import MarshmallowPlugin
from jinja2 import Template
from scalpl import Cut

from ..utils.decorators.singleton_decorator import singleton
from .security_scheme import apikey_header
from .security_scheme import jwt_header
from .utils import get_path_keys


@singleton
class OpenApi:
    """Auto generate Open API specification documents."""

    _DEFAULT_RESPONSE_LOCATION = "json"
    _VALID_RESPONSE_FIELDS = {"description", "headers", "examples"}
    _DOCUMENT_PATH = (
        Path().absolute().joinpath("src/viper_boot/openapi_docs")
    )

    def __init__(self) -> None:
        """Initialise Open API specs."""
        with open("./openapi.yml", encoding="utf8") as file_:
            yaml_settings = yaml.safe_load(file_)
            self._settings = Cut(yaml_settings)

        try:
            curr_api_ver = subprocess.check_output(
                ["git", "describe", "--tags", "--abbrev=0"]
            ).strip().decode()
        except BaseException:
            curr_api_ver = "0.0.1"

        title = self._settings["info.title"]
        api_version = curr_api_ver
        openapi_version = self._settings["openapi"]

        self._marshmallow_plugin = MarshmallowPlugin(
            schema_name_resolver=self._resolver
        )

        self._spec = APISpec(
            title=title,
            version=api_version,
            openapi_version=openapi_version,
            plugins=(self._marshmallow_plugin,),
            **self._settings,
        )

        # Add security scheme
        self.security_scheme()

        # Initialise document server
        self._index_page: str = ""
        self._server = _OpenApiServer

    def security_scheme(self) -> None:
        """Add Open API security scheme."""
        api_key_scheme: Dict[Any, Any] = apikey_header.security_header
        jwt_scheme: Dict[Any, Any] = jwt_header.security_header

        self._spec.components.security_scheme("api_key", api_key_scheme)
        self._spec.components.security_scheme("jwt", jwt_scheme)

    def generate_spec(self) -> Dict[str, Any]:
        """Generate Open API spec as JSON string.

        Returns:
            OpenAPI spec document
        """
        return self._spec.to_dict()

    def generate_doc(self) -> None:
        """Write Open API spec as JSON file."""
        try:
            os.remove("openapi_spec.json")
        except FileNotFoundError:
            pass

        with open("openapi_spec.json", "w", encoding="utf8") as outfile:
            json.dump(self.generate_spec(), outfile, indent=2)

    def serve_doc(self) -> None:
        """Serve Open API documents."""
        with open(
            self._DOCUMENT_PATH / "site" / "index.html", encoding="utf8"
        ) as template_index_html:
            self._index_page = Template(template_index_html.read()).render(
                path="openapi_spec.json",
                static=self._DOCUMENT_PATH / "site",
                spec=json.dumps(self.generate_spec(), indent=2),
            )

        host = self._settings["servers[0].variables.host.default"]
        port = self._settings["servers[0].variables.port.default"]

        open_api_server = HTTPServer((host, port), _OpenApiServer)

        try:
            print(f"OpenAPI server started http://{host}:{port}")
            open_api_server.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
        finally:
            open_api_server.server_close()

    @staticmethod
    def _resolver(schema: Any) -> Any:
        """Marshmallow plugin schema resolver.

        Parameters:
            schema (Any): schema object

        Returns:
            schema object
        """
        schema_instance = common.resolve_schema_instance(schema)
        prefix = "Partial-" if schema_instance.partial else ""
        # mypy: allow-untyped-calls
        schema_cls = common.resolve_schema_cls(schema)
        name = prefix + schema_cls.__name__
        if name.endswith("Schema"):
            _name = name[:-6] or name
            return _name
        return name

    def register(self, path: str, handler: Any) -> None:
        """Register handler with OpenApi spec.

        Parameters:
            path (str): API path
            handler (Any): handler function

        Returns:
            any value
        """
        if not hasattr(handler, "__apispec__"):
            return None

        data: Any = handler.__apispec__

        http_method = data.pop("method") or "get"
        http_method = http_method.lower()

        if http_method not in VALID_METHODS_OPENAPI_V2:
            return None

        for schema in data.pop("schemas", []):
            parameters = self._marshmallow_plugin.converter.schema2parameters(
                schema["schema"],
                location=schema["location"],
                **schema["options"],
            )
            self._add_examples(schema["schema"], parameters, schema["example"])
            data["parameters"].extend(parameters)

        existing = [p["name"] for p in data["parameters"] if p["in"] == "path"]

        data["parameters"].extend(
            {
                "in": "path",
                "name": path_key,
                "required": True,
                "type": "string",
            }
            for path_key in get_path_keys(path)
            if path_key not in existing
        )

        if "responses" in data:
            responses = {}
            for code, actual_params in data["responses"].items():
                if "schema" in actual_params:
                    raw_parameters = (
                        self._marshmallow_plugin.converter.schema2parameters(
                            actual_params["schema"],
                            location=self._DEFAULT_RESPONSE_LOCATION,
                            required=actual_params.get("required", False),
                        )[0]
                    )

                    updated_params = {
                        k: v
                        for k, v in raw_parameters.items()
                        if k in self._VALID_RESPONSE_FIELDS
                    }
                    updated_params["schema"] = actual_params["schema"]
                    for extra_info in self._VALID_RESPONSE_FIELDS:
                        if extra_info in actual_params:
                            updated_params[extra_info] = actual_params[
                                extra_info
                            ]
                    responses[code] = updated_params
                else:
                    responses[code] = actual_params
            data["responses"] = responses

        operations = copy.deepcopy(data)

        self._spec.path(path=path, operations={http_method: operations})

    def _add_examples(
        self, ref_schema: Any, endpoint_schema: Any, example: Any
    ) -> None:
        """Register handler with OpenApi spec.

        Parameters:
            ref_schema (Any): reference schema,
            endpoint_schema (Any): endpoint schema,
            example (Any): example schema,

        Returns:
            None
        """
        def add_to_endpoint_or_ref() -> None:
            """Add reference or endpoint to OpenAPI spec."""
            if add_to_refs:
                self.spec.components.schemas[name]["example"] = example
            else:
                endpoint_schema[0]["schema"]["allOf"] = [
                    endpoint_schema[0]["schema"].pop("$ref")
                ]
                endpoint_schema[0]["schema"]["example"] = example

        if not example:
            return
        schema_instance = common.resolve_schema_instance(ref_schema)
        name = self._marshmallow_plugin.converter.schema_name_resolver(
            schema_instance
        )
        add_to_refs = example.pop("add_to_refs")
        if self._spec.components.openapi_version.major < 3:
            if name and name in self._spec.components.schemas:
                add_to_endpoint_or_ref()
        else:
            add_to_endpoint_or_ref()

    @property
    def spec(self) -> Any:
        """Getter method for Open Api specs.

        Returns:
            Open Api specs object
        """
        return self._spec

    @property
    def index_page(self) -> Any:
        """Getter method for Open Api index html file.

        Returns:
            Open Api index html file
        """
        return self._index_page


class _OpenApiServer(BaseHTTPRequestHandler):
    """OpenAPI document server."""

    def do_GET(self) -> None:  # noqa # pylint: disable=C0103
        """Get request handler."""
        index_page = OpenApi().index_page
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(index_page, "utf-8"))
