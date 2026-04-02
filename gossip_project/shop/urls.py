from django.urls import path
from shop.views import HomepageDataView, NewsletterSubscribeView

urlpatterns = [
    path('', HomepageDataView.as_view(), name='homepage-data'),
    path('newsletter/', NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
]
