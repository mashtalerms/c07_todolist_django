from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validators


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=True, max_length=50)
    email = serializers.EmailField(required=True, max_length=50)
    first_name = serializers.CharField(required=False, max_length=50)
    last_name = serializers.CharField(required=False, max_length=50)
    password = serializers.CharField(required=True, write_only=True)

    def is_valid(self, raise_exception=False):
        self._password_repeat = self.initial_data.pop("password_repeat")
        return super().is_valid(raise_exception=raise_exception)

    def validate_username(self, value):
        if self.Meta.model.objects.filter(username=value).exists():
            raise serializers.ValidationError("User with this username already exists")
        return value

    def validate_password(self, value):
        validators.validate_password(value)
        return value

    def validate(self, data):
        if data.get("password") != self._password_repeat:
            raise serializers.ValidationError("Passwords must match")
        return data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(user.password)
        user.password_repeat = user.password
        user.save()

        return user

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password"]


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError("User with this username does not exist")
        return username


class UserRetrieveUpdateSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=False, max_length=50)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    email = serializers.EmailField(required=False, allow_blank=True)

    def validate_username(self, username):
        current_user = self.context["request"].user
        if self.Meta.model.objects.filter(username=username).exists() and current_user.username != username:
            raise serializers.ValidationError("User with this username does not exist")
        return username

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class PasswordUpdateSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validators.validate_password(value)
        return value
