from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from products.models import Product

class Order(models.Model):
    """
    Customer orders
    """
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    # Order Identification
    order_number = models.CharField(max_length=50, unique=True, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='orders'
    )
    
    # Status Tracking
    status = models.CharField(
        max_length=20, 
        choices=ORDER_STATUS_CHOICES, 
        default='pending'
    )
    payment_status = models.CharField(
        max_length=20, 
        choices=PAYMENT_STATUS_CHOICES, 
        default='pending'
    )
    
    # Pricing
    subtotal = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    shipping_cost = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    tax = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    discount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    total_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    
    # Shipping Information
    tracking_number = models.CharField(max_length=100, null=True, blank=True)
    estimated_delivery = models.DateField(null=True, blank=True)
    
    # Notes
    customer_notes = models.TextField(blank=True)
    admin_notes = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f"Order #{self.order_number} - {self.user.username}"
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            # Generate unique order number
            import random
            import string
            timestamp = self.created_at.strftime('%Y%m%d') if self.created_at else ''
            random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            self.order_number = f"ORD-{timestamp}-{random_suffix}"
        
        # Calculate total
        self.total_amount = self.subtotal + self.shipping_cost + self.tax - self.discount
        
        super().save(*args, **kwargs)
    
    @property
    def is_completed(self):
        return self.status == 'delivered'
    
    @property
    def can_cancel(self):
        return self.status in ['pending', 'processing']


class OrderItem(models.Model):
    """
    Individual items in an order
    """
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name='items'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.SET_NULL, 
        null=True
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )  # Price at time of purchase
    size = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name if self.product else 'Unknown Product'}"
    
    @property
    def total_price(self):
        return self.price * self.quantity


class ShippingAddress(models.Model):
    """
    Shipping address for orders
    """
    order = models.OneToOneField(
        Order, 
        on_delete=models.CASCADE, 
        related_name='shipping_address'
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Addresses'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.city}"


class BillingAddress(models.Model):
    """
    Billing address for orders
    """
    order = models.OneToOneField(
        Order, 
        on_delete=models.CASCADE, 
        related_name='billing_address'
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        verbose_name = 'Billing Address'
        verbose_name_plural = 'Billing Addresses'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.city}"
