from django.urls import path

from .views import UserCreateAPIView, UserDeleteAPIView, UserDetailAPIView, UserListAPIView, UserUpdateAPIView

app_name = "users"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user-list"),
    path("create/", UserCreateAPIView.as_view(), name="user-create"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user-update"),
    path("<int:pk>/delete/", UserDeleteAPIView.as_view(), name="user-delete"),
]
