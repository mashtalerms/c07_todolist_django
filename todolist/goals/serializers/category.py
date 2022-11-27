from rest_framework import serializers

from core.serializers import UserRetrieveUpdateSerializer
from goals.models.category import Category
from goals.models.participant import BoardParticipant


class CategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"

    def validate_board(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("not allowed in deleted board")

        user = value.participants.filter(user=self.context["request"].user).first()
        if not user:
            raise serializers.ValidationError("not owner or writer of the board")
        elif user.role not in [BoardParticipant.Role.owner, BoardParticipant.Role.writer]:
            raise serializers.ValidationError("not owner or writer of the board")

        return value


class CategorySerializer(serializers.ModelSerializer):
    user = UserRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user", "board")