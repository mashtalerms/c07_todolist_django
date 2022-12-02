import pytest


@pytest.mark.django_db
def test_update_password(client):
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

    new_password = 'newpass#@_maks12#!'

    update_password_response = client.put(
        '/core/update_password',
        {'old_password': user_data['password'], 'new_password': new_password},
        content_type='application/json')

    login_response = client.post(
        '/core/login',
        {'username': user_data['username'], 'password': new_password},
        content_type='application/json')

    assert create_user_response.status_code == 201
    assert login_user_response.status_code == 200
    assert update_password_response.status_code == 204
    assert login_response.status_code == 200
