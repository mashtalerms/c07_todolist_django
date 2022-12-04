import pytest

from goals.serializers.comment import CommentSerializer


@pytest.mark.django_db
def test_comment_retrieve(client, get_credentials, comment, board_participant):
	response = client.get(
		path=f'/goals/goal_comment/{comment.id}',
		HTTP_AUTHORIZATION=get_credentials
	)
	assert response.status_code == 200
	assert response.data == CommentSerializer(comment).data
