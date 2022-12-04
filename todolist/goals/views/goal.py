from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from goals.filters import GoalDateFilter
from goals.models.goal import Goal
from goals.permissions import GoalPermissions
from goals.serializers.goal import GoalCreateSerializer, GoalSerializer


class GoalCreateView(CreateAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated, GoalPermissions]
    serializer_class = GoalCreateSerializer


class GoalListView(ListAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    ordering_fields = ["due_date"]
    ordering = ["-priority", "due_date"]
    search_fields = ["title", "description"]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = GoalDateFilter

    def get_queryset(self) -> Goal:
        return Goal.objects.filter(
            category__board__participants__user=self.request.user, is_deleted=False
        )


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated, GoalPermissions]

    def get_queryset(self) -> Goal:
        return Goal.objects.filter(
            category__board__participants__user=self.request.user, is_deleted=False
        )

    def perform_destroy(self, instance: Goal) -> Goal:
        instance.is_deleted = True
        instance.status = 4
        instance.save()
        return instance
