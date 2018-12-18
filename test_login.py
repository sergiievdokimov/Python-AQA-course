import requests

base_url = 'https://python-qa-training.herokuapp.com/api/auth/login'
email = 'sievdokymov@lohika.com'
password = '12345678'

def login(email,password):
    res = requests.post(base_url, json={"email":email, "password":password})
    return res

def test_login_valid_credentials():
    assert login(email,password).status_code == 200

def test_login_invalid_email():
    email = "wrong@wrong.com"
    assert login(email,password).status_code == 404

def test_login_invalid_password():
        password = "wrong"
        assert login(email, password).status_code == 401 #unathorized

def test_login_empty_values():
    email = ""
    password = ""
    assert login(email, password).status_code == 404