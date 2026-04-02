from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    """
    Product categories (e.g., Designers, Clothing, Shoes, Bags, Accessories)
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE,
        related_name='children'
    )
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """
    Luxury fashion products - the heart of our e-commerce platform
    """
    # Basic Information
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    
    # Pricing
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    compare_at_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=True, 
        blank=True,
        help_text="Original price for showing discounts"
    )
    
    # Categorization
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='products'
    )
    brand = models.CharField(
        max_length=100,
        help_text="Designer/Brand name (e.g., Gucci, Prada, Chanel)"
    )
    
    # Inventory
    stock_quantity = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    
    # Variants
    sizes = models.JSONField(default=list, blank=True, help_text="Available sizes: ['XS', 'S', 'M', 'L', 'XL']")
    colors = models.JSONField(default=list, blank=True, help_text="Available colors: ['Black', 'White', 'Red']")
    
    # Product Details (Luxury-specific)
    material = models.CharField(max_length=255, blank=True, help_text="e.g., 100% Silk, Italian Leather")
    made_in = models.CharField(max_length=100, blank=True, help_text="Country of origin")
    care_instructions = models.TextField(blank=True)
    designer_bio = models.TextField(blank=True, help_text="Brief info about the designer")
    
    # Flags
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    is_new_arrival = models.BooleanField(default=False, help_text="New collection item")
    is_on_sale = models.BooleanField(default=False)
    discount_percentage = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(100)]
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_featured']),
            models.Index(fields=['is_new_arrival']),
        ]
    
    def __str__(self):
        return f"{self.name} - {self.brand}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        # Auto-calculate discount percentage
        if self.compare_at_price and self.price < self.compare_at_price:
            discount = ((self.compare_at_price - self.price) / self.compare_at_price) * 100
            self.discount_percentage = round(discount)
            self.is_on_sale = True
        
        super().save(*args, **kwargs)
    
    @property
    def has_discount(self):
        return self.is_on_sale and self.discount_percentage > 0
    
    @property
    def is_in_stock(self):
        return self.stock_quantity > 0


class ProductImage(models.Model):
    """
    Multiple images for a product
    """
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=255, blank=True)
    is_primary = models.BooleanField(default=False, help_text="Main product image")
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['display_order', '-is_primary']
    
    def __str__(self):
        return f"Image for {self.product.name}"
    
    def save(self, *args, **kwargs):
        # If this is set as primary, unset other primary images
        if self.is_primary:
            ProductImage.objects.filter(
                product=self.product, 
                is_primary=True
            ).exclude(pk=self.pk).update(is_primary=False)
        super().save(*args, **kwargs)
