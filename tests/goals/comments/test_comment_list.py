import pytest

from tests.factories import GoalCommentFactory
from goals.serializers.comment import CommentSerializer


@pytest.mark.django_db
def test_comment_list(client, get_credentials, goal, board_participant):
    comments = GoalCommentFactory.create_batch(10, user=goal.user, goal=goal)

    response = client.get(
        path='/goals/goal_comment/list',
        HTTP_AUTHORIZATION=get_credentials
    )

    assert response.status_code == 200
