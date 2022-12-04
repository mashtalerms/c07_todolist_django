import pytest


@pytest.mark.django_db
def test_category_create(client, get_credentials, user, board):
    data = {
        "title": "cat_test",
        "board": board.id,
        "user": user.id
    }

    response = client.post(
        path='/goals/goal_category/create',
        HTTP_AUTHORIZATION=get_credentials,
        data=data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data['title'] == data['title']
    assert response.data['board'] == data['board']
