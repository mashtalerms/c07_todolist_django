import pytest


@pytest.mark.django_db
def test_comment_create(client, create_goal):
    create_comment = client.post('/goals/goal_comment/create',
                                 {'text': 'test_comment',
                                  'goal': create_goal.data['id']},
                                 content_type='application/json')

    comment_response = client.get(f'/goals/goal_comment/{create_comment.data["id"]}')

    expected_response = {
        "id": create_comment.data['id'],
        "user": comment_response.data['user'],
        "created": create_comment.data['created'],
        "updated": create_comment.data['updated'],
        "text": "test_comment",
        "goal": create_goal.data['id']
    }

    assert create_comment.status_code == 201
    assert comment_response.status_code == 200
    assert comment_response.data == expected_response
