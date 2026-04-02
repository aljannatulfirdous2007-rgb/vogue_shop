from django.contrib import admin
from shop.models import Banner, FeaturedCollection, NewsletterSubscription

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'priority', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'subtitle']
    readonly_fields = ['image_preview']
    ordering = ['-priority']

@admin.register(FeaturedCollection)
class FeaturedCollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    filter_horizontal = ['products']

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_subscribed', 'subscribed_at']
    list_filter = ['is_subscribed', 'subscribed_at']
    search_fields = ['email']
