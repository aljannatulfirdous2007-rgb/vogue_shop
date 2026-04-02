from django.contrib import admin
from orders.models import Order, OrderItem, ShippingAddress, BillingAddress

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number', 'user', 'status', 'total_amount',
        'is_paid', 'created_at'
    ]
    list_filter = ['status', 'is_paid', 'created_at']
    search_fields = ['order_number', 'user__username', 'email']
    readonly_fields = ['order_number', 'total_amount']
    ordering = ['-created_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    list_filter = ['order', 'product']
    search_fields = ['product__name', 'order__order_number']

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address_line1', 'city', 'state', 'postal_code']
    search_fields = ['user__username', 'city', 'state']

@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address_line1', 'city', 'state', 'postal_code']
    search_fields = ['user__username', 'city', 'state']
