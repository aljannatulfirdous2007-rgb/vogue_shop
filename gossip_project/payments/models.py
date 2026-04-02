from django.db import models
from django.conf import settings
from orders.models import Order

class Payment(models.Model):
    """
    Payment transactions for orders
    """
    PAYMENT_METHOD_CHOICES = [
        ('stripe', 'Stripe (Credit Card)'),
        ('paypal', 'PayPal'),
        ('cod', 'Cash on Delivery'),
        ('bank_transfer', 'Bank Transfer'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
        ('disputed', 'Disputed'),
    ]
    
    # Order Reference
    order = models.OneToOneField(
        Order, 
        on_delete=models.CASCADE, 
        related_name='payment'
    )
    
    # Payment Details
    payment_method = models.CharField(
        max_length=20, 
        choices=PAYMENT_METHOD_CHOICES
    )
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    currency = models.CharField(max_length=3, default='USD')
    status = models.CharField(
        max_length=20, 
        choices=PAYMENT_STATUS_CHOICES, 
        default='pending'
    )
    
    # Stripe Specific Fields
    stripe_charge_id = models.CharField(max_length=255, null=True, blank=True)
    stripe_payment_intent_id = models.CharField(max_length=255, null=True, blank=True)
    stripe_receipt_url = models.URLField(null=True, blank=True)
    
    # PayPal Specific Fields
    paypal_payment_id = models.CharField(max_length=255, null=True, blank=True)
    paypal_payer_id = models.CharField(max_length=255, null=True, blank=True)
    
    # Metadata
    payment_gateway_response = models.JSONField(default=dict, blank=True)
    error_message = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    refunded_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Payment {self.transaction_id or self.id} - Order {self.order.order_number}"
    
    @property
    def is_successful(self):
        return self.status == 'completed'
    
    @property
    def can_refund(self):
        return self.status in ['completed']
