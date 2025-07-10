from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import CustomUser
from .permissions import IsActiveEmployee
from .serializers import CustomUserCreateSerializer, CustomUserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsActiveEmployee]  # Используем IsActiveEmployee

    def get_queryset(self):
        qs = super().get_queryset()
        if role := self.request.query_params.get("role", None):
            qs = qs.filter(role=role)
        return qs


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsActiveEmployee]  # Используем IsActiveEmployee


class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    permission_classes = [IsActiveEmployee, IsAdminUser]  # Активный сотрудник + админ


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsActiveEmployee]


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsActiveEmployee]
