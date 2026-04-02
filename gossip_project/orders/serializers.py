from rest_framework import serializers
from orders.models import Order, OrderItem, ShippingAddress, BillingAddress

class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for order items"""
    product_name = serializers.CharField(source='product.name', read_only=True)
    total_price = serializers.DecimalField(
        source='total_price',
        max_digits=10, 
        decimal_places=2,
        read_only=True
    )
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price', 'size', 'color', 'total_price']


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['first_name', 'last_name', 'address_line1', 'address_line2', 
                  'city', 'state', 'postal_code', 'country', 'phone', 'email']


class OrderCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating orders"""
    shipping_address = ShippingAddressSerializer()
    items = serializers.ListField(write_only=True)
    
    class Meta:
        model = Order
        fields = [
            'shipping_address', 'items', 'customer_notes'
        ]
    
    def create(self, validated_data):
        shipping_address_data = validated_data.pop('shipping_address')
        items_data = validated_data.pop('items')
        customer_notes = validated_data.get('customer_notes', '')
        
        # Calculate totals from cart items
        subtotal = sum(item['price'] * item['quantity'] for item in items_data)
        shipping_cost = 10.00  # Flat rate
        tax = subtotal * 0.1  # 10% tax
        
        # Create order
        order = Order.objects.create(
            user=self.context['request'].user,
            subtotal=subtotal,
            shipping_cost=shipping_cost,
            tax=tax,
            customer_notes=customer_notes,
        )
        
        # Create order items
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        # Create shipping address
        ShippingAddress.objects.create(order=order, **shipping_address_data)
        
        return order


class OrderSerializer(serializers.ModelSerializer):
    """Full order serializer"""
    items = OrderItemSerializer(many=True, read_only=True)
    shipping_address = ShippingAddressSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'status', 'status_display', 'payment_status',
            'subtotal', 'shipping_cost', 'tax', 'discount', 'total_amount',
            'items', 'shipping_address', 'tracking_number', 'estimated_delivery',
            'customer_notes', 'created_at', 'is_completed', 'can_cancel'
        ]
