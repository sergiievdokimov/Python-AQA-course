import rest_client
import json_provider
from random import randint


def test_create_issue_valid(login, delete_issue):
    summary = "New issue summary"
    description = "Description of the new issue"
    priority = randint(1, 5)
    response = rest_client.create_issue(json_provider.create_issue_json(summary, description, priority), login)
    json = response.json()
    assert response.status_code == 201
    assert json['summary'] == summary
    assert json['description'] == description
    assert json['priority'] == priority


def test_create_issue_missed_summary(login):
    summary = None
    description = "Description of the new issue"
    priority = randint(1, 5)
    response = rest_client.create_issue(json_provider.create_issue_json(summary, description, priority), login)
    assert response.status_code == 422


def test_create_issue_missed_description(login):
    summary = 'New issue summary'
    description = None
    priority = randint(1, 5)
    response = rest_client.create_issue(json_provider.create_issue_json(summary, description, priority), login)
    assert response.status_code == 422


def test_create_issue_missed_priority(login):
    summary = 'New issue summary'
    description = 'Description of the new issue'
    priority = None
    response = rest_client.create_issue(json_provider.create_issue_json(summary, description, priority), login)
    assert response.status_code == 422


def test_create_issue_wrong_priority(login):
    summary = "New issue summary"
    description = "Description of the new issue"
    priority = 6
    response = rest_client.create_issue(json_provider.create_issue_json(summary, description, priority), login)
    assert response.status_code == 422
