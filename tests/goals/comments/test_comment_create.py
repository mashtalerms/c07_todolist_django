import pytest


@pytest.mark.django_db
def test_comment_create(client, get_credentials, goal, board_participant):
    data = {
        'text': 'text',
        'goal': goal.id,
    }

    response = client.post(
        path='/goals/goal_comment/create',
        HTTP_AUTHORIZATION=get_credentials,
        data=data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data['text'] == data['text']
    assert response.data['goal'] == data['goal']
