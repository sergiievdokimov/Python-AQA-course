import rest_client
import json_provider
from data import Valid_User, Invalid_User


def test_login_valid_credentials():
    response = rest_client.login(json_provider.login_json(Valid_User.email, Valid_User.password))
    assert response.status_code == 200
    assert response.json()['token'] is not None


def test_login_invalid_email():
    response = rest_client.login(json_provider.login_json(Invalid_User.email, Valid_User.password))
    assert response.status_code == 401


def test_login_invalid_password():
    response = rest_client.login(json_provider.login_json(Invalid_User.email, Valid_User.password))
    assert response.status_code == 401


def test_login_invalid_email_and_invalid_password():
    response = rest_client.login(json_provider.login_json(Invalid_User.email, Invalid_User.password))
    assert response.status_code == 401
