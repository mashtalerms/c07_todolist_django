from django.urls import path

from goals.views.board import BoardCreateView, BoardListView, BoardView
from goals.views.category import CategoryCreateView, CategoryListView, CategoryView
from goals.views.comment import CommentCreateView, CommentListView, CommentView
from goals.views.goal import GoalCreateView, GoalListView, GoalView

urlpatterns = [
    path("goal_category/create", CategoryCreateView.as_view()),
    path("goal_category/list", CategoryListView.as_view()),
    path("goal_category/<pk>", CategoryView.as_view()),
    path("goal/create", GoalCreateView.as_view()),
    path("goal/list", GoalListView.as_view()),
    path("goal/<pk>", GoalView.as_view()),
    path("goal_comment/create", CommentCreateView.as_view()),
    path("goal_comment/list", CommentListView.as_view()),
    path("goal_comment/<pk>", CommentView.as_view()),
    path("board/create", BoardCreateView.as_view()),
    path("board/list", BoardListView.as_view()),
    path("board/<pk>", BoardView.as_view()),

]
