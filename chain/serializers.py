from rest_framework import serializers

from chain.models import Product, Supplier


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "product_name", "model", "release_date"]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ["debt"]
        extra_kwargs = {"debt": {"required": True}}
