from rest_framework import serializers
from products.models import Product, Category, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer for product images"""
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_primary', 'display_order']


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for categories"""
    children = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'parent', 'children', 'is_active']
    
    def get_children(self, obj):
        if hasattr(obj, 'children'):
            return CategorySerializer(obj.children.all(), many=True).data
        return []


class ProductListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for product listing"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    primary_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'brand', 'price', 'compare_at_price',
            'category', 'category_name', 'category_slug',
            'primary_image', 'is_new_arrival', 'is_featured', 'is_on_sale',
            'discount_percentage', 'stock_quantity', 'created_at'
        ]
    
    def get_primary_image(self, obj):
        image = obj.images.filter(is_primary=True).first()
        if image:
            return image.image.url
        elif obj.images.exists():
            return obj.images.first().image.url
        return None


class ProductDetailSerializer(serializers.ModelSerializer):
    """Full serializer for product details"""
    images = ProductImageSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    related_products = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            # Basic Info
            'id', 'name', 'slug', 'description', 'brand',
            
            # Pricing
            'price', 'compare_at_price', 'has_discount', 'discount_percentage',
            
            # Categorization
            'category', 'category_name',
            
            # Inventory
            'stock_quantity', 'is_in_stock', 'sku',
            
            # Variants
            'sizes', 'colors',
            
            # Luxury Details
            'material', 'made_in', 'care_instructions', 'designer_bio',
            
            # Flags
            'is_featured', 'is_new_arrival', 'is_on_sale',
            
            # Media
            'images',
            
            # Related
            'related_products',
            
            # Timestamps
            'created_at', 'updated_at',
        ]
    
    def get_related_products(self, obj):
        """Get 4 related products from same category"""
        if obj.category:
            related = Product.objects.filter(
                category=obj.category,
                is_featured=True
            ).exclude(id=obj.id)[:4]
            return ProductListSerializer(related, many=True).data
        return []
