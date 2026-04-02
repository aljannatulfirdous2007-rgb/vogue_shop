"""
URL configuration for gossip_project_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 🔐 JWT Token endpoints - your VIP pass to the party!
from rest_framework_simplejwt.views import (
    TokenRefreshView,     # Refresh your token (extend your VIP status)
)
# Import custom login view from users app
from users.views import LoginAPIView

urlpatterns = [
    # Admin site - where the head Plastic rules!
    path('admin/', admin.site.urls),
    
    # 🔐 JWT Authentication Endpoints
    # POST /api/token/ - Get your access token (your VIP wristband!)
    # Uses custom LoginAPIView that accepts username OR email
    path('api/token/', LoginAPIView.as_view(), name='token_obtain_pair'),
    
    # POST /api/token/refresh/ - Refresh your token (renew that VIP status!)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # 👥 Users App URLs - for user management
    path('api/users/', include('users.urls')),
    
    # 💼 E-COMMERCE API ENDPOINTS - Vogue-style luxury fashion
    path('api/products/', include('products.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/homepage/', include('shop.urls')),
]
