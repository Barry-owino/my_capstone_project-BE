from rest_framework import serializers
from .models import Transaction
from books_app.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'book', 'checkout_date', 'return_date']
        read_only_fields = ['checkout_date', 'return_date', 'id'] #to prevent modification of checkout and return date fields


