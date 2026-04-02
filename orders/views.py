from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderCreateSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing orders
    
    Actions:
    - list: GET /api/orders/ - List user's orders
    - create: POST /api/orders/create/ - Create new order
    - retrieve: GET /api/orders/<id>/ - Get order details
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer
    
    def create(self, request, *args, **kwargs):
        """Create order from cart"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Create order
        order = serializer.save(user=request.user)
        
        # In a real app, you would:
        # 1. Clear the user's cart
        # 2. Process payment
        # 3. Send confirmation email
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
