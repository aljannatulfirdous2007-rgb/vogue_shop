from django.contrib import admin
from products.models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'is_active', 'created_at']
    list_filter = ['is_active', 'parent']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
        return "No image"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'brand', 'category', 'price', 'stock_quantity',
        'is_featured', 'is_new_arrival', 'is_on_sale', 'created_at'
    ]
    list_filter = [
        'category', 'brand', 'is_featured', 'is_new_arrival', 
        'is_on_sale', 'stock_quantity'
    ]
    search_fields = ['name', 'description', 'brand', 'sku']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-created_at']
    inlines = [ProductImageInline]
    readonly_fields = ['has_discount', 'discount_percentage']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'brand', 'category')
        }),
        ('Pricing', {
            'fields': ('price', 'compare_at_price', 'discount_percentage', 'has_discount')
        }),
        ('Inventory', {
            'fields': ('stock_quantity', 'sku')
        }),
        ('Variants', {
            'fields': ('sizes', 'colors')
        }),
        ('Luxury Details', {
            'fields': ('material', 'made_in', 'care_instructions', 'designer_bio')
        }),
        ('Flags', {
            'fields': ('is_featured', 'is_new_arrival', 'is_on_sale')
        }),
    )
