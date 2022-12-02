import pytest


@pytest.mark.django_db
def test_category_create(client, user_csrf):
    board_create = client.post(
        '/goals/board/create',
        {"title": "test_board_create"},
        content_type='application/json')

    board_detail_response = client.get(f'/goals/board/{int(board_create.data["id"])}')

    create_category = client.post('/goals/goal_category/create',
                                  {'title': 'test_category_create',
                                   'board': {int(board_create.data["id"])}},
                                  format='json')

    response = client.get(f"/goals/goal_category/{int(create_category.data['id'])}",
                          format='json')

    expected_response = {
        "id": create_category.data["id"],
        "user": user_csrf[0].data,
        "created": create_category.data["created"],
        "updated": create_category.data["updated"],
        "title": "test_category_create",
        "is_deleted": False,
        "board": board_create.data["id"]
    }

    assert board_create.status_code == 201
    assert board_detail_response.status_code == 200
    assert create_category.status_code == 201
    assert response.status_code == 200
    assert response.data == expected_response
