import pytest

from tests.factories import GoalFactory
from todolist.goals.serializers.goal import GoalSerializer


@pytest.mark.django_db
def test_goal_list(client, get_credentials, board_participant, goal__category):
    goals = GoalFactory.create_batch(10, user=board_participant.user, category=goal__category)

    response = client.get(
        path='/goals/goal/list',
        HTTP_AUTHORIZATION=get_credentials
    )

    assert response.status_code == 200
    assert response.data == GoalSerializer(goals, many=True).data
