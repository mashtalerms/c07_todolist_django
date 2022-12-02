import pytest


@pytest.mark.django_db
def test_category_list(client, user_csrf):
    board_create = client.post(
        '/goals/board/create',
        {'title': 'test_board_create'},
        content_type='application/json')

    board_detail_response = client.get(f'/goals/board/{int(board_create.data["id"])}')

    create_category_1 = client.post('/goals/goal_category/create',
                                    {'title': 'test_category_1',
                                     'board': {int(board_create.data["id"])}},
                                    format='json')

    create_category_2 = client.post('/goals/goal_category/create',
                                    {'title': 'test_category_2',
                                     'board': {int(board_create.data["id"])}},
                                    format='json')

    expected_response = [
        {
            "id": create_category_1.data['id'],
            "user": user_csrf[0].data,
            "created": create_category_1.data['created'],
            "updated": create_category_1.data['updated'],
            "title": 'test_category_1',
            "is_deleted": False,
            "board": board_create.data['id']
        },
        {
            "id": create_category_2.data['id'],
            "user": user_csrf[0].data,
            "created": create_category_2.data['created'],
            "updated": create_category_2.data['updated'],
            "title": 'test_category_2',
            "is_deleted": False,
            "board": board_create.data['id']
        }]

    response = client.get(f'/goals/goal_category/list',
                          format='json')

    assert board_create.status_code == 201
    assert board_detail_response.status_code == 200
    assert response.status_code == 200
    assert response.data == expected_response
