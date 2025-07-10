from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Пользователь"""

    EMPLOYEE = "employee"
    INACTIVE_EMPLOYEE = "inactive_employee"
    ADMIN = "admin"

    ROLE_CHOICES = [
        (EMPLOYEE, "Сотрудник"),
        (INACTIVE_EMPLOYEE, "Неактивный сотрудник"),
        (ADMIN, "Администратор"),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=INACTIVE_EMPLOYEE)

    @property
    def is_active_employee(self):
        return self.role == self.EMPLOYEE

    @property
    def is_inactive_employee(self):
        return self.role == self.INACTIVE_EMPLOYEE

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
