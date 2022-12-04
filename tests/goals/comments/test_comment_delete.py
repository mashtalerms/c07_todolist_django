import pytest


@pytest.mark.django_db
def test_comment_delete(client, get_credentials, comment, board_participant):
    response = client.delete(
        path=f'/goals/goal_comment/{comment.id}',
        HTTP_AUTHORIZATION=get_credentials,
    )
    assert response.status_code == 204
    assert response.data is None
