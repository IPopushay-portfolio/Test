from django.contrib import admin

from .models import Product, Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["supplier_name", "chain_type", "city", "get_hierarchy_level", "debt"]
    list_filter = ["chain_type", "city", "country"]
    search_fields = ["supplier_name", "city"]
    raw_id_fields = ["supplier", "products"]

    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "model", "release_date"]
    search_fields = ["product_name", "model"]
