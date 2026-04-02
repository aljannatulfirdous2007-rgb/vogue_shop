from django.urls import path
from .views import UserListView  # import your ListView here

from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserListView, LoginAPIView
urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'),  # /api/users/list/
    path('token/', LoginAPIView.as_view(), name='token_obtain_pair'),  # /api/users/token/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # /api/users/token/refresh/
]
