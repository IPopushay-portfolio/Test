from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

User = get_user_model()


# Product
class Product(models.Model):

    product_name = models.CharField(max_length=200, verbose_name="Название продукта")
    model = models.CharField(max_length=200, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return f"{self.product_name} ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        unique_together = ("product_name", "model")


class Supplier(models.Model):
    CONNECTION_TYPES = (
        ("factory", "Завод"),
        ("retail", "Розничная сеть"),
        ("entrepreneur", "Индивидуальный предприниматель"),
    )

    supplier_name = models.CharField(max_length=200, verbose_name="Название поставщика")
    chain_type = models.CharField(max_length=20, choices=CONNECTION_TYPES, verbose_name="Тип цепочки")

    def __str__(self):
        return f"{self.supplier_name} ({self.get_chain_type_display()})"

    def get_hierarchy_level(self):
        """Получение уровня иерархии"""
        if self.chain_type == "factory":
            return 0
        elif self.supplier:
            return self.supplier.get_hierarchy_level() + 1
        return 1

    get_hierarchy_level.short_description = "Уровень иерархии"

    # Контактная информация
    email = models.EmailField(unique=True, verbose_name="Email")
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=200, verbose_name="Город")
    street = models.CharField(max_length=200, verbose_name="Улица")
    building_number = models.CharField(max_length=100, verbose_name="Номер дома")

    products = models.ManyToManyField(Product, verbose_name="Продукты", related_name="suppliers")

    supplier = models.ForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, verbose_name="Поставщик", related_name="clients"
    )

    debt = models.DecimalField(
        decimal_places=2, max_digits=20, default=Decimal("0.00"), verbose_name="Задолженность перед поставщиком"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def clean(self):
        if self.chain_type == "factory" and self.supplier:
            raise ValidationError("Завод не может иметь поставщика")

        if self.supplier and self.chain_type == "factory":
            raise ValidationError("Неверный тип цепочки для данного уровня иерархии")

    class Meta:
        verbose_name = "Поставщик"  # Изменено название
        verbose_name_plural = "Поставщики"
        ordering = ["supplier_name"]
