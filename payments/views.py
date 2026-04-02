from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import stripe
from django.conf import settings
from payments.models import Payment
from orders.models import Order

class PaymentIntentView(APIView):
    """
    Create Stripe payment intent
    POST /api/payments/create-intent/
    
    Body: { "order_id": 123 }
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        order_id = request.data.get('order_id')
        
        if not order_id:
            return Response(
                {'error': 'Order ID required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            
            # Set your secret key (in production, use environment variable)
            stripe.api_key = settings.STRIPE_SECRET_KEY or 'sk_test_YOUR_KEY'
            
            # Create payment intent
            intent = stripe.PaymentIntent.create(
                amount=int(order.total_amount * 100),  # Amount in cents
                currency='usd',
                metadata={
                    'order_id': order.order_number,
                    'user_id': request.user.id,
                }
            )
            
            return Response({
                'client_secret': intent.client_secret,
                'payment_intent_id': intent.id,
            })
        
        except Order.DoesNotExist:
            return Response(
                {'error': 'Order not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
