import pytest

from tests.factories import GoalCategoryFactory
from goals.serializers.category import CategorySerializer


@pytest.mark.django_db
def test_category_list(client, get_credentials, board_participant):
	categories = GoalCategoryFactory.create_batch(10, user=board_participant.user, board=board_participant.board)

	response = client.get(
		path='/goals/goal_category/list',
		HTTP_AUTHORIZATION=get_credentials
	)

	assert response.status_code == 200
	assert response.data == CategorySerializer(categories, many=True).data
