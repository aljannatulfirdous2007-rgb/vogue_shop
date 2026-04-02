from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet, WishlistViewSet

router = DefaultRouter()
router.register(r'', ReviewViewSet, basename='review')
router.register(r'wishlist', WishlistViewSet, basename='wishlist')

urlpatterns = [
    path('', include(router.urls)),
]
