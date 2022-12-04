from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from goals.models.category import Category
from goals.models.goal import Goal
from goals.serializers.category import CategoryCreateSerializer, CategorySerializer
from goals.permissions import GoalCategoryPermissions


class CategoryCreateView(CreateAPIView):
    model = Category
    permission_classes = [permissions.IsAuthenticated, GoalCategoryPermissions]
    serializer_class = CategoryCreateSerializer


class CategoryListView(ListAPIView):
    model = Category
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]
    filterset_fields = ["board"]

    def get_queryset(self) -> Category:
        return Category.objects.filter(
            board__participants__user=self.request.user, is_deleted=False
        )


class CategoryView(RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, GoalCategoryPermissions]

    def get_queryset(self) -> Category:
        return Category.objects.filter(
            board__participants__user=self.request.user, is_deleted=False
        )

    def perform_destroy(self, instance: Category) -> Category:
        instance.is_deleted = True
        goals = Goal.objects.filter(category=instance)

        for goal in goals:
            goal.is_deleted = True
            goal.status = 4

        instance.save()
        return instance
