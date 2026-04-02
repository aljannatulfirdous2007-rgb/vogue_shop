from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from products.models import Product

class Cart(models.Model):
    """
    Shopping cart for each user
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Shopping Cart'
        verbose_name_plural = 'Shopping Carts'
    
    def __str__(self):
        return f"Cart for {self.user.username}"
    
    @property
    def total_items(self):
        """Total number of items in cart"""
        return sum(item.quantity for item in self.items.all())
    
    @property
    def subtotal(self):
        """Total price before tax and shipping"""
        return sum(item.get_total_price() for item in self.items.all())
    
    def add_item(self, product, quantity=1, size=None, color=None):
        """
        Add product to cart or update quantity if already exists
        """
        try:
            # Check if item already exists with same variant
            item = self.items.get(
                product=product, 
                size=size, 
                color=color
            )
            item.quantity += quantity
            item.save()
        except CartItem.DoesNotExist:
            # Create new item
            item = CartItem.objects.create(
                cart=self,
                product=product,
                quantity=quantity,
                size=size,
                color=color
            )
        return item
    
    def update_item_quantity(self, product_id, quantity, size=None, color=None):
        """
        Update quantity of a specific item
        """
        try:
            item = self.items.get(
                product_id=product_id,
                size=size,
                color=color
            )
            if quantity <= 0:
                item.delete()
            else:
                item.quantity = quantity
                item.save()
            return True
        except CartItem.DoesNotExist:
            return False
    
    def remove_item(self, item_id):
        """Remove item from cart"""
        try:
            item = self.items.get(id=item_id)
            item.delete()
            return True
        except CartItem.DoesNotExist:
            return False
    
    def clear(self):
        """Empty the cart"""
        self.items.all().delete()


class CartItem(models.Model):
    """
    Individual items in the shopping cart
    """
    cart = models.ForeignKey(
        Cart, 
        on_delete=models.CASCADE, 
        related_name='items'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
    size = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['cart', 'product', 'size', 'color']
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    def get_total_price(self):
        """Total price for this item"""
        return self.product.price * self.quantity
