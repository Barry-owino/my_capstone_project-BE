from django.urls import path
from .views import CheckoutBookView, ReturnBookView, TransactionListView

urlpatterns = [
    path('checkout/<int:book_id>/', CheckoutBookView.as_view(), name='checkout-book'),
    path('return/<int:book_id>/', ReturnBookView.as_view(), name='return-book'),
    path('', TransactionListView.as_view(), name='transaction-list'),
]
