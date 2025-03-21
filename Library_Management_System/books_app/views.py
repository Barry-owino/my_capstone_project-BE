from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# this view class list all books or create a new book.
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#this view retrieve, update, or delete a single book
class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
