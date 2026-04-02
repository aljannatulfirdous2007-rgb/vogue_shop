from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product

class Review(models.Model):
    """
    Customer reviews for products
    """
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='reviews'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    
    # Rating
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    # Review Content
    title = models.CharField(max_length=200)
    comment = models.TextField()
    
    # Verification
    verified_purchase = models.BooleanField(default=False)
    
    # Engagement
    helpful_count = models.PositiveIntegerField(default=0)
    not_helpful_count = models.PositiveIntegerField(default=0)
    
    # Moderation
    is_approved = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['product', 'user']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return f"{self.rating}★ - {self.title} by {self.user.username}"
    
    @property
    def helpful_percentage(self):
        total = self.helpful_count + self.not_helpful_count
        if total == 0:
            return 0
        return (self.helpful_count / total) * 100


class Wishlist(models.Model):
    """
    User's wishlist/favorites
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='wishlist'
    )
    products = models.ManyToManyField(
        Product, 
        related_name='wishlists',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'
    
    def __str__(self):
        return f"Wishlist of {self.user.username}"
    
    def add_product(self, product):
        """Add product to wishlist"""
        self.products.add(product)
    
    def remove_product(self, product):
        """Remove product from wishlist"""
        self.products.remove(product)
    
    def is_in_wishlist(self, product):
        """Check if product is in wishlist"""
        return self.products.filter(id=product.id).exists()
