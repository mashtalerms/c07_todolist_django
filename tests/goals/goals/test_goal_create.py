import pytest


@pytest.mark.django_db
def test_goal_create(client, create_category):
    create_goal = client.post(
         '/goals/goal/create', {'title': 'test_goal', 'category': create_category.data['id']},
         content_type='application/json')

    goal_response = client.get(f'/goals/goal/{int(create_goal.data["id"])}')

    expected_response = {
        "id": create_goal.data['id'],
        "category": create_category.data['id'],
        "created": create_goal.data['created'],
        "updated": create_goal.data['updated'],
        "title": "test_goal",
        "description": None,
        "status": create_goal.data['status'],
        "priority": create_goal.data['priority'],
        "due_date": create_goal.data['due_date'],
        "user": goal_response.data['user'],
        "is_deleted": goal_response.data['is_deleted']
    }

    assert create_goal.status_code == 201
    assert goal_response.status_code == 200
    assert goal_response.data == expected_response
