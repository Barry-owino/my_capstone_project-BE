#from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# this view class list all books or create a new book.
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'author', 'isbn']

    def get_queryset(self):
        queryset = Book.objects.all()

        available = self.request.query_params.get('available')
        if available and available.lower() == "true":
            queryset = queryset.filter(copies_available__gt=0)

        return queryset

#this view retrieve, update, or delete a single book
class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
