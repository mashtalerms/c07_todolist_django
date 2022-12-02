import pytest

from core.models import User


@pytest.mark.django_db
def test_update_user_profile(client):
    user_data = {
        'username': 'test_maks1',
        'first_name': 'test_maks1',
        'last_name': 'test_maks1',
        'email': 'test_maks1@test.ru',
        'password': 'test#@_maks12#!',
        'password_repeat': 'test#@_maks12#!'
    }

    create_user_response = client.post(
        '/core/signup',
        data=user_data,
        content_type='application/json')

    login_user_response = client.post(
        '/core/login',
        {'username': user_data['username'], 'password': user_data['password']},
        content_type='application/json')

    user_after_update = User.objects.get(username=user_data['username'])

    update_user_response = client.patch(
        '/core/profile',
        {'first_name': 'UPDATE'},
        content_type='application/json')

    user_before_update = User.objects.get(username=user_data['username'])

    assert create_user_response.status_code == 201
    assert login_user_response.status_code == 200
    assert create_user_response.data['first_name'] == user_data['first_name']
    assert update_user_response.status_code == 200
    assert user_after_update.first_name != user_before_update.first_name
    assert user_before_update.first_name == 'UPDATE'
