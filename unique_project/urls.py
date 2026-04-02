from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # include the shop app URLs
    path('api/users/', include('users.urls')),  # include users app URLs
]
