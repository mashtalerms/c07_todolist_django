import pytest


@pytest.fixture()
@pytest.mark.django_db
def user_csrf(client, django_user_model):
    """Create user and login him"""
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

    return create_user_response, login_user_response


@pytest.fixture
def create_board(client, user_csrf):
    """Board creation fixture"""
    create_board_response = client.post(
        '/goals/board/create',
        data={'title': 'test_board'},
        content_type='application/json')
    return create_board_response


@pytest.fixture
def create_category(client, create_board):
    """Category creation fixture"""
    create_category = client.post('/goals/goal_category/create',
                                  {'title': 'test_category',
                                   'board': create_board.data["id"]},
                                  format='json')

    return create_category


@pytest.fixture
def create_goal(client, create_category):
    """Goal creation fixture"""
    create_goal = client.post('/goals/goal/create',
                              {'title': 'test_goal', 'category': create_category.data['id']},
                              content_type='application/json')
    return create_goal
