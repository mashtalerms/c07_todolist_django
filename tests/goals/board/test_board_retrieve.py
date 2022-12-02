import pytest


@pytest.mark.django_db
def test_board_retrieve(client, user_csrf):
    board_create_response = client.post(
        "/goals/board/create",
        {"title": "test_board_create"},
        content_type='application/json'
    )

    board_retrieve_response = client.get(
        f"/goals/board/{int(board_create_response.data['id'])}"
    )
    expected_response = {
        "id": board_create_response.data["id"],
        "participants": board_retrieve_response.data["participants"],
        "created": board_create_response.data["created"],
        "updated": board_create_response.data["updated"],
        "title": board_create_response.data["title"],
        "is_deleted": False
    }

    assert board_create_response.status_code == 201
    assert board_retrieve_response.status_code == 200
    assert board_retrieve_response.data == expected_response
