import pytest


@pytest.mark.django_db
def test_goal_delete(client, get_credentials, goal, board_participant):
    response = client.delete(
        path=f'/goals/goal/{goal.id}',
        HTTP_AUTHORIZATION=get_credentials,
    )

    assert response.status_code == 204
    assert response.data is None
