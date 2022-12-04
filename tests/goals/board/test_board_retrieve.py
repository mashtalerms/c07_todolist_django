import pytest

from goals.serializers.board import BoardSerializer


@pytest.mark.django_db
def test_board_retrieve(client, get_credentials, board, board_participant):
    response = client.get(
        path=f'/goals/board/{board.id}',
        HTTP_AUTHORIZATION=get_credentials
    )

    assert response.status_code == 200
    assert response.data == BoardSerializer(board).data
