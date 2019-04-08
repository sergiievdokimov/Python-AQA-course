import pytest
from data import Valid_User, Invalid_User
import rest_client

valid_user = Valid_User()
invalid_user = Invalid_User()


@pytest.mark.parametrize("email, password, expected_status_code", [
    (valid_user.email, valid_user.password, 200),
    (valid_user.email, invalid_user.password, 401),
    (invalid_user.email, valid_user.password, 401),
    (invalid_user.email, invalid_user.password, 401),
    ('', '', 401),
])
def test_login(email, password, expected_status_code, json):
    assert rest_client.login(json.login_json(email, password)).status_code == expected_status_code
