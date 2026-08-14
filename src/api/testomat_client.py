from typing import Any
from urllib.parse import quote

from playwright.sync_api import (
    APIRequestContext,
    APIResponse,
    Error as PlaywrightError,
)


class TestomatConfigurationError(ValueError):
    """Raised when required Testomat client configuration is missing."""


class TestomatResponseError(RuntimeError):
    """Raised when Testomat returns an unexpected response payload."""


class TestomatClient:
    """Client for authenticated requests to the Testomat user API."""

    DEFAULT_BASE_URL = "https://app.testomat.io"

    def __init__(
        self,
        api_token: str | None,
        request_context: APIRequestContext,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 10.0,
    ) -> None:
        if not api_token or not api_token.strip():
            raise TestomatConfigurationError(
                "TESTOMAT_API_TOKEN is missing or empty. Add a general Testomat "
                "API token to the local .env file."
            )

        self._api_token = api_token.strip()
        self._request_context = request_context
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._jwt: str | None = None

    def authenticate(self) -> str:
        """Exchange the general API token for a JWT used by user API requests."""
        response = self._fetch(
            "POST",
            "/api/login",
            data={"api_token": self._api_token},
        )

        payload = self._decode_object(response, "Login")
        jwt = payload.get("jwt")
        if not isinstance(jwt, str) or not jwt.strip():
            raise TestomatResponseError(
                "Login response did not contain a non-empty 'jwt' value."
            )

        self._jwt = jwt.strip()
        return self._jwt

    def get_projects(self) -> dict[str, Any]:
        """Return all projects available to the authenticated Testomat user."""
        response = self._request("GET", "/api/projects")
        return self._decode_object(response, "Projects")

    def get_suites(self, project_id: str) -> dict[str, Any]:
        """Return the suites available in a project."""
        response = self._request("GET", f"/api/{self._segment(project_id)}/suites")
        return self._decode_object(response, "Suites")

    def create_suite(self, project_id: str, title: str) -> dict[str, Any]:
        """Create a root suite in a project."""
        response = self._request(
            "POST",
            f"/api/{self._segment(project_id)}/suites",
            data={
                "data": {
                    "type": "suites",
                    "attributes": {"title": title},
                }
            },
        )
        return self._decode_object(response, "Create suite")

    def delete_suite(self, project_id: str, suite_id: str) -> None:
        """Delete a suite from a project."""
        self._request(
            "DELETE",
            f"/api/{self._segment(project_id)}/suites/{self._segment(suite_id)}",
        )

    def create_test(
        self,
        project_id: str,
        suite_id: str,
        title: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        """Create a test in a project suite."""
        attributes = {
            "title": title,
            "suite_id": suite_id,
        }
        if description is not None:
            attributes["description"] = description

        response = self._request(
            "POST",
            f"/api/{self._segment(project_id)}/tests",
            data={
                "data": {
                    "type": "tests",
                    "attributes": attributes,
                }
            },
        )
        return self._decode_object(response, "Create test")

    def get_test(self, project_id: str, test_id: str) -> dict[str, Any]:
        """Return a test and its dependencies."""
        response = self._request(
            "GET",
            f"/api/{self._segment(project_id)}/tests/{self._segment(test_id)}",
        )
        return self._decode_object(response, "Test")

    def delete_test(self, project_id: str, test_id: str) -> None:
        """Delete a test from a project."""
        self._request(
            "DELETE",
            f"/api/{self._segment(project_id)}/tests/{self._segment(test_id)}",
        )

    def _request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> APIResponse:
        if self._jwt is None:
            self.authenticate()

        headers = dict(kwargs.pop("headers", {}))
        headers["Authorization"] = f"Bearer {self._jwt}"
        return self._fetch(method, path, headers=headers, **kwargs)

    def _fetch(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> APIResponse:
        try:
            response = self._request_context.fetch(
                f"{self._base_url}{path}",
                method=method,
                timeout=self._timeout * 1000,
                **kwargs,
            )
        except PlaywrightError as error:
            raise TestomatResponseError(
                f"{method} {path} failed: {error}"
            ) from error

        if not response.ok:
            raise TestomatResponseError(
                f"{method} {path} returned HTTP {response.status} "
                f"{response.status_text}."
            )
        return response

    @staticmethod
    def _segment(value: str) -> str:
        if not value or not value.strip():
            raise TestomatConfigurationError("API resource ID is missing or empty.")
        return quote(value.strip(), safe="")

    @staticmethod
    def _decode_object(
        response: APIResponse,
        response_name: str,
    ) -> dict[str, Any]:
        try:
            payload = response.json()
        except ValueError as error:
            raise TestomatResponseError(
                f"{response_name} response was not valid JSON."
            ) from error

        if not isinstance(payload, dict):
            raise TestomatResponseError(
                f"{response_name} response must be a JSON object."
            )
        return payload
