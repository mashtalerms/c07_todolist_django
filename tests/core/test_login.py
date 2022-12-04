import pytest


@pytest.mark.django_db
def test_login(client):
    signup_data = {
        "username": "test_username",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "email": "test_email@test.ru",
        "password": "test_password",
        "password_repeat": "test_password"
    }
    signup_response = client.post(
        "/core/signup",
        signup_data,
        content_type='application/json')

    login_data = {
        "username": "test_username",
        "password": "test_password"
    }
    response = client.post(
        "/core/login",
        login_data,
        content_type='application/json')

    assert signup_response.status_code == 201
    assert response.status_code == 200
