from uuid import uuid4

import pytest


TARGET_PROJECT_TITLE = "python manufacture"


@pytest.fixture
def projects(api_client):
    payload = api_client.get_projects()

    assert "data" in payload, "Projects response must include JSON:API 'data'."
    project_items = payload["data"]
    assert isinstance(project_items, list), "Projects 'data' must be a list."
    return project_items


@pytest.fixture
def project_id(projects):
    for project in projects:
        if not isinstance(project, dict):
            continue
        attributes = project.get("attributes")
        if (
            isinstance(attributes, dict)
            and attributes.get("title") == TARGET_PROJECT_TITLE
        ):
            selected_project_id = project.get("id")
            assert selected_project_id not in (None, ""), (
                f"Project '{TARGET_PROJECT_TITLE}' must have an ID."
            )
            return str(selected_project_id)

    pytest.fail(
        f"Project '{TARGET_PROJECT_TITLE}' was not found for the authenticated user.",
        pytrace=False,
    )


def test_get_projects_for_authenticated_user(projects):
    for project in projects:
        assert isinstance(project, dict), "Each project must be a JSON object."
        assert project.get("id") not in (None, ""), "Each project must have an ID."


def test_open_project_and_create_test(api_client, projects, project_id):
    assert any(
        isinstance(project, dict) and project.get("id") == project_id
        for project in projects
    )

    suites_payload = api_client.get_suites(project_id)
    assert "data" in suites_payload, "Suites response must include JSON:API 'data'."
    assert isinstance(suites_payload["data"], list), "Suites 'data' must be a list."

    unique_suffix = uuid4().hex[:8]
    suite_title = f"API test suite {unique_suffix}"
    test_title = f"API test case {unique_suffix}"

    suite_payload = api_client.create_suite(project_id, suite_title)
    suite = _resource_data(suite_payload, "Created suite")
    suite_id = _resource_id(suite, "Created suite")

    try:
        test_payload = api_client.create_test(
            project_id=project_id,
            suite_id=suite_id,
            title=test_title,
            description="Temporary test created by the API integration test.",
        )
        created_test = _resource_data(test_payload, "Created test")
        test_id = _resource_id(created_test, "Created test")

        try:
            created_attributes = created_test.get("attributes")
            assert isinstance(created_attributes, dict)
            assert created_attributes.get("title") == test_title

            fetched_payload = api_client.get_test(project_id, test_id)
            fetched_test = _resource_data(fetched_payload, "Fetched test")
            assert fetched_test.get("id") == test_id

            fetched_attributes = fetched_test.get("attributes")
            assert isinstance(fetched_attributes, dict)
            assert fetched_attributes.get("title") == test_title
            assert fetched_attributes.get("suite-id") == suite_id
        finally:
            api_client.delete_test(project_id, test_id)
    finally:
        api_client.delete_suite(project_id, suite_id)


def _resource_data(payload, resource_name):
    resource = payload.get("data")
    assert isinstance(resource, dict), f"{resource_name} 'data' must be an object."
    return resource


def _resource_id(resource, resource_name):
    resource_id = resource.get("id")
    assert resource_id not in (None, ""), f"{resource_name} must have an ID."
    return str(resource_id)
