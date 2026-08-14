import os
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest
from playwright.sync_api import APIRequestContext, Playwright

from src.api import TestomatClient as ApiClient


@pytest.fixture
def api_request_context(playwright: Playwright) -> Iterator[APIRequestContext]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


@pytest.fixture
def api_client(api_request_context: APIRequestContext) -> ApiClient:
    return ApiClient(
        api_token=os.getenv("TESTOMAT_API_TOKEN"),
        request_context=api_request_context,
    )


@pytest.fixture(autouse=True)
def api_trace(
    api_client: ApiClient,
    api_request_context: APIRequestContext,
    output_path: str,
    pytestconfig: pytest.Config,
    request: pytest.FixtureRequest,
) -> Iterator[Any | None]:
    tracing_option = pytestconfig.getoption("--tracing")
    if tracing_option == "off":
        yield None
        return

    # Keep the general API token out of the trace. Authenticated requests can
    # still contain a bearer JWT, so generated traces must remain private.
    api_client.authenticate()
    tracing = api_request_context.tracing
    tracing.start(
        title=request.node.nodeid,
        snapshots=True,
        sources=True,
    )

    try:
        yield tracing
    finally:
        failed = not hasattr(request.node, "rep_call") or request.node.rep_call.failed
        retain_trace = tracing_option == "on" or (
            tracing_option == "retain-on-failure" and failed
        )

        if retain_trace:
            trace_path = Path(output_path) / "api-trace.zip"
            trace_path.parent.mkdir(parents=True, exist_ok=True)
            tracing.stop(path=trace_path)
        else:
            tracing.stop()
