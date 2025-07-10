from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра пользователя"""

    class Meta:
        model = CustomUser
        fields = ["username", "email", "role"]


class CustomUserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания пользователя"""

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "role"]
