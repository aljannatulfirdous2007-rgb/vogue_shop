from rest_framework import serializers
from shop.models import Banner, FeaturedCollection
from products.serializers import ProductListSerializer

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'id', 'title', 'subtitle', 'description', 
            'image', 'cta_text', 'cta_link'
        ]


class FeaturedCollectionSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)
    
    class Meta:
        model = FeaturedCollection
        fields = ['id', 'name', 'slug', 'description', 'cover_image', 'products']
