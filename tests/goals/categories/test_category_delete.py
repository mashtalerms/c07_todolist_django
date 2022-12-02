import pytest


@pytest.mark.django_db
def test_board_delete(client, user_csrf):
    board_create_response = client.post(
        "/goals/board/create",
        {"title": "test_board_create"},
        content_type='application/json'
    )
    board_delete_response = client.delete(
        f"/goals/board/{int(board_create_response.data['id'])}",
        content_type='application/json'
    )

    assert board_create_response.status_code == 201
    assert board_delete_response.status_code == 204
