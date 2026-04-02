from rest_framework import serializers
from reviews.models import Review, Wishlist
from products.serializers import ProductListSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id', 'product', 'user', 'user_name', 'rating',
            'title', 'comment', 'verified_purchase',
            'helpful_count', 'is_approved', 'created_at'
        ]
        read_only_fields = ['user', 'verified_purchase', 'is_approved']


class WishlistSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)
    product_count = serializers.IntegerField(source='products.count', read_only=True)
    
    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'products', 'product_count', 'created_at']
