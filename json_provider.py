def login_json(email: str, password: str):
    return {"email": email, "password": password}

def create_issue_json(summary: str, description: str, priority: int):
    json = {}
    if summary:
        json['summary'] = summary
    if description:
        json['description'] = description
    if priority:
        json['priority'] = priority

    return json

