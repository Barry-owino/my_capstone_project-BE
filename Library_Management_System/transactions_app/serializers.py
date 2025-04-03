from rest_framework import serializers
from .models import Transaction
from books_app.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

class TransactionSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_author = serializers.CharField(source='book.author', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'book', 'book_title', 'book_author', 'checkout_date', 'return_date']
        read_only_fields = ['checkout_date', 'return_date', 'id'] #to prevent modification of checkout and return date fields


