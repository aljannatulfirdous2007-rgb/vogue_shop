from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from products.models import Product, Category
from products.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    CategorySerializer,
)

class ProductListView(generics.ListCreateAPIView):
    """
    List all products or create a new product
    GET /api/products/
    POST /api/products/
    
    Filters:
    - category: Filter by category slug
    - brand: Filter by brand name
    - min_price, max_price: Price range filter
    - is_new_arrival: Filter new arrivals only
    - is_featured: Filter featured products only
    
    Search: Search by name, description, brand
    Order: By created_at, price, name
    """
    queryset = Product.objects.select_related('category').prefetch_related('images').all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category__slug', 'brand', 'is_new_arrival', 'is_featured']
    search_fields = ['name', 'description', 'brand']
    ordering_fields = ['created_at', 'price', 'name']
    ordering = ['-created_at']  # Newest first
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductDetailSerializer
        return ProductListSerializer
    
    def get_permissions(self):
        """Only authenticated users can create products"""
        if self.request.method == 'POST':
            return [IsAuthenticatedOrReadOnly()]
        return [AllowAny()]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        # Filter by sale items
        is_on_sale = self.request.query_params.get('is_on_sale')
        if is_on_sale and is_on_sale.lower() == 'true':
            queryset = queryset.filter(is_on_sale=True)
        
        return queryset


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a single product
    GET /api/products/{slug}/
    PUT/PATCH /api/products/{slug}/
    DELETE /api/products/{slug}/
    """
    queryset = Product.objects.select_related('category').prefetch_related('images').all()
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        return ProductDetailSerializer
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticatedOrReadOnly()]
        return [AllowAny()]


class CategoryListView(generics.ListAPIView):
    """
    List all active categories
    GET /api/products/categories/
    """
    queryset = Category.objects.filter(is_active=True).prefetch_related('children').all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
