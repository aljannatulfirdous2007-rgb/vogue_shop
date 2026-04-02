from django.contrib import admin
from reviews.models import Review, Wishlist

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'product', 'user', 'rating', 'is_verified_purchase',
        'is_approved', 'created_at'
    ]
    list_filter = ['rating', 'is_verified_purchase', 'is_approved', 'created_at']
    search_fields = ['product__name', 'user__username', 'comment']
    readonly_fields = ['is_verified_purchase']
    ordering = ['-created_at']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_products_count', 'created_at']
    search_fields = ['user__username', 'products__name']
    readonly_fields = ['products']
    
    def get_products_count(self, obj):
        return obj.products.count()
    get_products_count.short_description = 'Products'
