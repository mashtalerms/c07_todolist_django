import pytest


@pytest.mark.django_db
def test_goal_update(client, get_credentials, goal, board_participant):
    new_title = 'updated_title'

    response = client.patch(
        path=f'/goals/goal/{goal.id}',
        HTTP_AUTHORIZATION=get_credentials,
        data={'title': new_title},
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.data.get('title') == new_title
