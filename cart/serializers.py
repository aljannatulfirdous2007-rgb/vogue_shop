from rest_framework import serializers
from cart.models import Cart, CartItem
from products.serializers import ProductListSerializer

class CartItemSerializer(serializers.ModelSerializer):
    """Serializer for individual cart items"""
    product = ProductListSerializer(read_only=True)
    total_price = serializers.DecimalField(
        source='get_total_price',
        max_digits=10, 
        decimal_places=2,
        read_only=True
    )
    
    class Meta:
        model = CartItem
        fields = [
            'id', 'product', 'quantity', 'size', 'color',
            'total_price', 'added_at'
        ]


class CartSerializer(serializers.ModelSerializer):
    """Serializer for shopping cart"""
    items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.IntegerField(read_only=True)
    subtotal = serializers.DecimalField(
        source='subtotal',
        max_digits=10, 
        decimal_places=2,
        read_only=True
    )
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_items', 'subtotal', 'created_at', 'updated_at']
