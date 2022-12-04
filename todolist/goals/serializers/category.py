from rest_framework import serializers

from core.serializers import UserRetrieveUpdateSerializer
from goals.models.category import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    user = UserRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user", "board")
