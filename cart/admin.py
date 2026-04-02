from django.contrib import admin
from cart.models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_items', 'subtotal', 'created_at', 'updated_at']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['total_items', 'subtotal']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', 'size', 'color', 'get_total_price']
    list_filter = ['cart', 'product']
    search_fields = ['product__name', 'cart__user__username']
