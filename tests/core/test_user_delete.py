import pytest


@pytest.mark.django_db
def test_delete_user(client):

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

    user_delete_response = client.delete(
        '/core/profile',
    )

    assert create_user_response.status_code == 201
    assert login_user_response.status_code == 200
    assert user_delete_response.status_code == 200
