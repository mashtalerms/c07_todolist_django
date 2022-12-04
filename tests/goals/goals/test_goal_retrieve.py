import pytest

from goals.serializers.goal import GoalSerializer


@pytest.mark.django_db
def test_goal_retrieve(client, get_credentials, goal, user, board_participant):
	response = client.get(
		path=f'/goals/goal/{goal.id}',
		HTTP_AUTHORIZATION=get_credentials
	)

	assert response.status_code == 200
	assert response.data == GoalSerializer(goal).data
