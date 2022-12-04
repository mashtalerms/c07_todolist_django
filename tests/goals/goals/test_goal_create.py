import pytest


@pytest.mark.django_db
def test_goal_create(client, get_credentials, user, goal__category):
    data = {
        'title': 'title',
        'description': 'description',
        'user': user.id,
        'category': goal__category.id,
        'status': 2,
        'priority': 3,
        'due_date': '2022-11-15',
    }

    response = client.post(
        path='/goals/goal/create',
        HTTP_AUTHORIZATION=get_credentials,
        data=data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data['title'] == data['title']
    assert response.data['description'] == data['description']
    assert response.data['category'] == data['category']
    assert response.data['status'] == data['status']
    assert response.data['priority'] == data['priority']
    assert response.data['due_date'] == data['due_date']
