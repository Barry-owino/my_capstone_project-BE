from django.urls import path
from .views import CheckoutBookView, ReturnBookView

urlpatterns = [
    path('books/<int:book_id>/checkout/', CheckoutBookView.as_view(), name='checkout-book'),
    path('books/<int:book_id>/return/', ReturnBookView.as_view(), name='return_book'),
]
