from django.urls import path
from .views import CheckoutBookView, ReturnBookView

urlpatterns = [
    path('checkout/<int:book_id>/', CheckoutBookView.as_view(), name='checkout-book'),
    path('return/<int:book_id>/', ReturnBookView.as_view(), name='return-book'),
]
