from rest_framework import serializers

from core.serializers import UserRetrieveUpdateSerializer
from goals.models.goal import Goal
from goals.models.participant import BoardParticipant


class GoalSerializer(serializers.ModelSerializer):
    user = UserRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("not allowed in deleted category")

        if value.user != self.context["request"].user:
            raise serializers.ValidationError("not owner of category")

        return value
