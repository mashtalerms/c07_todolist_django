import pytest

from core.models import User


@pytest.mark.django_db
def test_signup_repeated_username(client):

    User.objects.create(username="test_username", password="test_password")

    data = {
        "username": "test_username",
        "password": "test_password",
        "password_repeat": "test_password"
    }

    response = client.post(
        "/core/signup",
        data,
        content_type='application/json')

    assert response.status_code == 400
    assert response.data == {"username": ["User with such username already exists"]}
