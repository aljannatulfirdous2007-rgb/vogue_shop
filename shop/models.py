from django.db import models
from django.utils.text import slugify
from products.models import Product

class Banner(models.Model):
    """
    Homepage hero banners (Vogue-style editorial banners)
    """
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    # Visual
    image = models.ImageField(upload_to='banners/')
    overlay_color = models.CharField(
        max_length=20, 
        default='rgba(0,0,0,0.4)',
        help_text="Overlay color for text readability"
    )
    
    # Call to Action
    cta_text = models.CharField(max_length=50, default='Shop Now')
    cta_link = models.CharField(
        max_length=500, 
        blank=True,
        help_text="URL or product category link"
    )
    
    # Display Settings
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class FeaturedCollection(models.Model):
    """
    Curated collections (Vogue-style editorials)
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    
    # Visual
    cover_image = models.ImageField(upload_to='collections/')
    
    # Products in Collection
    products = models.ManyToManyField(
        Product,
        related_name='collections',
        limit_choices_to={'is_featured': True}
    )
    
    # Display Settings
    is_featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order']
        verbose_name = 'Featured Collection'
        verbose_name_plural = 'Featured Collections'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class NewsletterSubscription(models.Model):
    """
    Newsletter subscribers
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    
    # Preferences
    wants_fashion_updates = models.BooleanField(default=True)
    wants_exclusive_offers = models.BooleanField(default=True)
    
    # Status
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'
    
    def __str__(self):
        return self.email
