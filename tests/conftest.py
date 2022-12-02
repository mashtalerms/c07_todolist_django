from pytest_factoryboy import register

from tests.factories.board import BoardFactory

pytest_plugins = "tests.fixtures"

register(BoardFactory)
