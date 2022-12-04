import pytest


@pytest.mark.django_db
def test_board_create(client, get_credentials, user):
    data = {
        'title': 'title',
        'user': user.id,
    }

    response = client.post(
        path='/goals/board/create',
        HTTP_AUTHORIZATION=get_credentials,
        data=data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data['title'] == data['title']
