from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from goals.models.comment import Comment
from goals.permissions import CommentPermissions
from goals.serializers.comment import CommentCreateSerializer, CommentSerializer


class CommentCreateView(CreateAPIView):
    model = Comment
    permission_classes = [permissions.IsAuthenticated, CommentPermissions]
    serializer_class = CommentCreateSerializer


class CommentListView(ListAPIView):
    model = Comment
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticated, CommentPermissions]
    ordering = ["-created"]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["goal"]

    def get_queryset(self) -> Comment:
        return Comment.objects.filter(goal__category__board__participants__user=self.request.user)


class CommentView(RetrieveUpdateDestroyAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, CommentPermissions]

    def get_queryset(self) -> Comment:
        return Comment.objects.filter(goal__category__board__participants__user=self.request.user)
