from django_filters import rest_framework as filters

from chain.models import Supplier


class SupplierFilter(filters.FilterSet):
    """Фильтры для поставщиков"""

    city = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Supplier
        fields = ["city"]
