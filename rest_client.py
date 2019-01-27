import requests

base_url = 'https://python-qa-training.herokuapp.com/api'
login_endpoint = "/auth/login"
issues = "/issues"
flaky = "/flaky"


def login(json: dict):
    return requests.post(url=base_url+login_endpoint, json=json)


def get_issues(token):
    headers = {'x-access-token': token}
    return requests.get(url=base_url+issues, headers=headers)


def create_issue(json: dict, token):
    headers = {'x-access-token': token}
    return requests.post(url=base_url+issues, headers=headers, json=json)


def update_issue(token: str, issue_id: str, json: dict):
    headers = {'x-access-token': token}
    path = "{}{}/{}".format(base_url, issues, issue_id)
    return requests.patch(url=path, headers=headers, json=json)


def find_issue(token, issue_id: str):
    headers = {'x-access-token': token}
    path = "{}{}/{}".format(base_url, issues, issue_id)
    return requests.get(url=path, headers=headers)


def delete_issue(token, issue_id: str):
    headers = {'x-access-token': token}
    path = "{}{}/{}".format(base_url, issues, issue_id)
    return requests.delete(url=path, headers=headers)
