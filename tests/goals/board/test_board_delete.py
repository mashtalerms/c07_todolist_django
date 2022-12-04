import pytest


@pytest.mark.django_db
def test_board_delete(client, get_credentials, board, board_participant):
    response = client.delete(
        path=f'/goals/board/{board.id}',
        HTTP_AUTHORIZATION=get_credentials,
    )

    assert response.status_code == 204
    assert response.data is None
