import pytest

from tests.factories import GoalCategoryFactory
from goals.serializers.category import CategorySerializer


@pytest.mark.django_db
def test_category_retrieve(client, get_credentials, goal__category, board_participant):
	response = client.get(
		path=f'/goals/goal_category/{goal__category.id}',
		HTTP_AUTHORIZATION=get_credentials
	)

	assert response.status_code == 200
	assert response.data == CategorySerializer(goal__category).data
