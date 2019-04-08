import pytest
import json_provider
import rest_client
from data import Valid_User, Invalid_User

# @pytest.fixture()
# #user (with email & password)

@pytest.fixture(scope="session")
def valid_user():
    return Valid_User


@pytest.fixture(scope="session")
def json():
    return json_provider


@pytest.fixture(scope="session")
def client():
    return rest_client


@pytest.fixture(scope="session")
def login(client):
    return client.login(json_provider.login_json(Valid_User.email, Valid_User.password)).json()['token']


@pytest.fixture(scope="function")
def create_issue(client, login, request):
    try:
        description = request.param['description']
    except (AttributeError, KeyError):
        description = "fixture description"
    try:
        summary = request.param['summary']
    except (AttributeError, KeyError):
        summary = "fixture summary"
    try:
        priority = request.param['priority']
    except (AttributeError, KeyError):
        priority = 1

    response = client.create_issue(json_provider.create_issue_json(summary, description, priority), login)
    return response


@pytest.fixture(scope="function")
def delete_issue(create_issue, client, login):
    yield delete_issue
    client.delete_issue(create_issue.json()['_id'], login)


