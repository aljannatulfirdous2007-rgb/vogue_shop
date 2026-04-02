from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CategoryListView,
)

urlpatterns = [
    # Product endpoints
    path('', ProductListView.as_view(), name='product-list'),  # GET all products, POST new product
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),  # GET/PUT/PATCH/DELETE single product
    
    # Category endpoints
    path('categories/', CategoryListView.as_view(), name='category-list'),  # GET all categories
]
