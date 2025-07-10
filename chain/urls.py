from django.urls import path

from chain.views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    SupplierCreateView,
    SupplierDeleteView,
    SupplierDetailView,
    SupplierListView,
    SupplierUpdateView,
)

app_name = "chain"

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    path("suppliers/", SupplierListView.as_view(), name="supplier-list"),
    path("suppliers/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
    path("suppliers/create/", SupplierCreateView.as_view(), name="supplier-create"),
    path("suppliers/<int:pk>/update/", SupplierUpdateView.as_view(), name="supplier-update"),
    path("suppliers/<int:pk>/delete/", SupplierDeleteView.as_view(), name="supplier-delete"),
]
