from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from reviews.models import Review, Wishlist
from reviews.serializers import ReviewSerializer, WishlistSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for product reviews
    
    Actions:
    - list: GET /api/reviews/?product=<id> - List reviews (optionally filter by product)
    - create: POST /api/reviews/ - Create review
    - update/partial_update: PUT/PATCH /api/reviews/<id>/ - Update review
    - destroy: DELETE /api/reviews/<id>/ - Delete review
    - mark_helpful: POST /api/reviews/<id>/mark_helpful/ - Mark review as helpful
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = Review.objects.filter(is_approved=True)
        
        # Filter by product if specified
        product_id = self.request.query_params.get('product')
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def mark_helpful(self, request, pk=None):
        review = self.get_object()
        review.helpful_count += 1
        review.save()
        return Response({'status': 'helpful count incremented'})


class WishlistViewSet(viewsets.ViewSet):
    """
    ViewSet for managing wishlist
    
    Actions:
    - list: GET /api/wishlist/ - Get user's wishlist
    - add: POST /api/wishlist/add/?product_id=<id> - Add product to wishlist
    - remove: DELETE /api/wishlist/remove/?product_id=<id> - Remove product
    """
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def add(self, request):
        product_id = request.data.get('product_id')
        
        if not product_id:
            return Response(
                {'error': 'Product ID required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            from products.models import Product
            product = Product.objects.get(id=product_id)
            
            wishlist, created = Wishlist.objects.get_or_create(user=request.user)
            wishlist.add_product(product)
            
            serializer = WishlistSerializer(wishlist)
            return Response(serializer.data)
        
        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['delete'])
    def remove(self, request):
        product_id = request.query_params.get('product_id')
        
        if not product_id:
            return Response(
                {'error': 'Product ID required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            product = Wishlist.objects.get(user=request.user).products.get(id=product_id)
            wishlist = Wishlist.objects.get(user=request.user)
            wishlist.remove_product(product)
            
            serializer = WishlistSerializer(wishlist)
            return Response(serializer.data)
        
        except Wishlist.DoesNotExist:
            return Response(
                {'error': 'Wishlist not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not in wishlist'}, 
                status=status.HTTP_404_NOT_FOUND
            )
