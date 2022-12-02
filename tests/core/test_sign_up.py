import pytest

from core.models import User


@pytest.mark.django_db
def test_signup(client):

    data = {
        "username": "test_username",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "email": "test_email@test.ru",
        "password": "test_password",
        "password_repeat": "test_password"
    }

    response = client.post(
        "/core/signup",
        data,
        content_type='application/json')

    user = User.objects.filter(username=data['username']).first()

    assert response.status_code == 201
    assert user.username == data['username']
