import pytest

from goals.serializers.board import BoardListSerializer

from tests.factories import BoardParticipantFactory, BoardFactory


@pytest.mark.django_db
def test_board_list(client, get_credentials, board_participant):
    boards = [board_participant.board]
    boards.extend(BoardFactory.create_batch(10))
    for board in boards[1:]:
        BoardParticipantFactory.create(user=board_participant.user, board=board)
    boards.sort(key=lambda x: x.title)

    response = client.get(
        path='/goals/board/list',
        HTTP_AUTHORIZATION=get_credentials
    )

    assert response.status_code == 200
    assert response.data == BoardListSerializer(boards, many=True).data
