import factory

from core.models import User

from goals.models.board import Board
from goals.models.category import Category
from goals.models.comment import Comment
from goals.models.goal import Goal
from goals.models.participant import BoardParticipant


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    first_name = 'Test name'
    last_name = 'Test name'
    email = 'email@mail.ru'
    password = 'fdsfds2542g'


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker('name')
    is_deleted = False


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardParticipant

    board = factory.SubFactory(BoardFactory)
    user = factory.SubFactory(UserFactory)
    role = 1


class GoalCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = 'Test'
    is_deleted = False
    user = factory.SubFactory(UserFactory)
    board = factory.SubFactory(BoardFactory)


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    title = 'Test'
    description = 'Test description'
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(GoalCategoryFactory)
    is_deleted = False
    status = 1
    priority = 2
    due_date = '2022-11-14'


class GoalCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = 'test com'
    goal = factory.SubFactory(GoalFactory)
    user = factory.SubFactory(UserFactory)
