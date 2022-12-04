import pytest


@pytest.mark.django_db
def test_category_delete(client, get_credentials, goal__category, board_participant):
    response = client.delete(
        path=f'/goals/goal_category/{goal__category.id}',
        HTTP_AUTHORIZATION=get_credentials,
    )

    assert response.status_code == 204
    assert response.data is None
