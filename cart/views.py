from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from cart.models import Cart, CartItem
from cart.serializers import CartSerializer, CartItemSerializer

class CartViewSet(viewsets.ViewSet):
    """
    ViewSet for managing shopping cart
    
    Actions:
    - list: GET /api/cart/ - Retrieve user's cart
    - add: POST /api/cart/add/ - Add item to cart
    - update: POST /api/cart/update/ - Update item quantity
    - remove: DELETE /api/cart/remove/<id>/ - Remove item from cart
    - clear: DELETE /api/cart/clear/ - Empty the cart
    """
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def list(self, request):
        """Get or create user's cart"""
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def add(self, request):
        """Add product to cart"""
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        size = request.data.get('size')
        color = request.data.get('color')
        
        if not product_id:
            return Response(
                {'error': 'Product ID is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            from products.models import Product
            product = Product.objects.get(id=product_id)
            
            # Add to cart
            cart.add_item(product, quantity, size, color)
            
            # Serialize and return updated cart
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['post'], url_path='update-item')
    def update_item(self, request):
        """Update item quantity in cart"""
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response(
                {'error': 'Cart not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        size = request.data.get('size')
        color = request.data.get('color')
        
        success = cart.update_item_quantity(product_id, quantity, size, color)
        
        if success:
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        else:
            return Response(
                {'error': 'Item not found in cart'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['delete'], url_path='remove/(?P<item_id>[0-9]+)')
    def remove(self, request, item_id=None):
        """Remove specific item from cart"""
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response(
                {'error': 'Cart not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        success = cart.remove_item(item_id)
        
        if success:
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        else:
            return Response(
                {'error': 'Item not found in cart'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['delete'])
    def clear(self, request):
        """Empty the cart"""
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart.clear()
            return Response({'message': 'Cart cleared'})
        
        return Response(
            {'error': 'Cart not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
