import pytest


@pytest.mark.django_db
def test_comment_update(client, get_credentials, comment, board_participant):
    new_text = 'updated_text'

    response = client.patch(
        path=f'/goals/goal_comment/{comment.id}',
        HTTP_AUTHORIZATION=get_credentials,
        data={'text': new_text},
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.data.get('text') == new_text
