from datetime import datetime

import pytest


@pytest.mark.django_db
def test_board_create(client, user_csrf):
    board_response = client.post(
        "/goals/board/create",
        {"title": "test_board_create"},
        content_type='application/json'
    )

    expected_response = {
        "id": board_response.data['id'],
        "created": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        "updated": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        "title": "test_board_create",
        "is_deleted": False
    }

    assert board_response.status_code == 201
    assert board_response.data['title'] == expected_response['title']
    assert board_response.data['id'] == expected_response['id']
    assert board_response.data['created'][0:19] == expected_response['created']
    assert board_response.data['updated'][0:19] == expected_response['updated']
    assert board_response.data['is_deleted'] == expected_response['is_deleted']
