from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from shop.models import Banner, FeaturedCollection, NewsletterSubscription
from products.models import Product
from shop.serializers import BannerSerializer, FeaturedCollectionSerializer

class HomepageDataView(APIView):
    """
    Get all homepage data in one request
    GET /api/homepage/
    
    Returns: banners, featured collections, new arrivals, featured products
    """
    permission_classes = [AllowAny]
    
    def get(self, request):
        # Get active banners
        banners = Banner.objects.filter(is_active=True)
        
        # Get featured collections
        collections = FeaturedCollection.objects.filter(
            is_active=True, 
            is_featured=True
        ).prefetch_related('products')
        
        # Get new arrivals
        new_arrivals = Product.objects.filter(
            is_new_arrival=True,
            stock_quantity__gt=0
        )[:8]
        
        # Get featured products
        featured_products = Product.objects.filter(
            is_featured=True,
            stock_quantity__gt=0
        )[:12]
        
        data = {
            'banners': BannerSerializer(banners, many=True).data,
            'collections': FeaturedCollectionSerializer(collections, many=True).data,
            'new_arrivals': self._serialize_products(new_arrivals),
            'featured_products': self._serialize_products(featured_products),
        }
        
        return Response(data)
    
    def _serialize_products(self, products):
        from products.serializers import ProductListSerializer
        return ProductListSerializer(products, many=True).data


class NewsletterSubscribeView(APIView):
    """
    Subscribe to newsletter
    POST /api/homepage/newsletter/
    
    Body: { "email": "user@example.com", "first_name": "John" }
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response(
                {'error': 'Email is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            subscriber, created = NewsletterSubscription.objects.get_or_create(
                email=email,
                defaults={'first_name': request.data.get('first_name', '')}
            )
            
            if not created:
                return Response(
                    {'message': 'Already subscribed'}, 
                    status=status.HTTP_200_OK
                )
            
            return Response(
                {'message': 'Successfully subscribed!'}, 
                status=status.HTTP_201_CREATED
            )
        
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
