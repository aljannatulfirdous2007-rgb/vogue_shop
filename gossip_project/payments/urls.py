from django.urls import path
from payments.views import PaymentIntentView

urlpatterns = [
    path('create-intent/', PaymentIntentView.as_view(), name='payment-intent'),
]
