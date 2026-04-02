from django.contrib import admin
from payments.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'order', 'amount', 'payment_method',
        'status', 'created_at'
    ]
    list_filter = ['status', 'payment_method', 'created_at']
    search_fields = ['transaction_id', 'user__username', 'order__order_number']
    readonly_fields = ['transaction_id', 'payment_intent_id', 'amount']
    ordering = ['-created_at']
