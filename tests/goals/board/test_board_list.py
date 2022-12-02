import pytest


@pytest.mark.django_db
def test_board_list(client, user_csrf):

    board_response_1 = client.post(
        "/goals/board/create",
        {"title": "test_board_create_1"},
        content_type='application/json'
    )
    board_response_2 = client.post(
        "/goals/board/create",
        {"title": "test_board_create_2"},
        content_type='application/json'
    )
    board_response_3 = client.post(
        "/goals/board/create",
        {"title": "test_board_create_3"},
        content_type='application/json'
    )

    expected_response = [
        {
        "id": board_response_1.data["id"],
        "created": board_response_1.data["created"],
        "updated": board_response_1.data["updated"],
        "title": board_response_1.data["title"],
        "is_deleted": False
        },
        {
        "id": board_response_2.data["id"],
        "created": board_response_2.data["created"],
        "updated": board_response_2.data["updated"],
        "title": board_response_2.data["title"],
        "is_deleted": False
        },
        {
        "id": board_response_3.data["id"],
        "created": board_response_3.data["created"],
        "updated": board_response_3.data["updated"],
        "title": board_response_3.data["title"],
        "is_deleted": False
    }
    ]

    boards_list_response = client.get(
        "/goals/board/list",
    )

    assert board_response_1.status_code == 201
    assert board_response_2.status_code == 201
    assert board_response_3.status_code == 201
    assert boards_list_response.data == expected_response


