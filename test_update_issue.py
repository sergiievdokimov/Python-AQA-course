import rest_client
import json_provider


def test_update_issue_summary_and_priority(client, login, create_issue, json, delete_issue):
    issue_id = create_issue.json()['_id']
    description = create_issue.json()['description']
    updated_summary = "Updated summary"
    updated_priority = 2
    response = rest_client.update_issue(issue_id=issue_id, json=json_provider.create_issue_json(summary=updated_summary, priority=updated_priority, description=description), token=login)
    assert response.status_code == 200
    assert response.json()['summary'] == updated_summary
    assert response.json()['priority'] == updated_priority
    assert response.json()['date_created'] != response.json()['date_updated']
