#from django.shortcuts import render
from rest_framework import generics, filters, permissions
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #allows only authenticated users to modify

    def perform_update(self, serializer):
        """prevent updating ISBN and ensure copies are available before updating"""
        instance = self.get_object()

        #prevent isbn updates
        if 'isbn' in self.request.data and self.request.data['isbn'] != instance.isbn:
            raise ValidationError({"isbn": "You cannot change the ISBN of a book."})

        #ensure book is available before updating
        if 'copies_available' in self.request.data and int(self.request.data['copies_available']) < 0:
            raise ValidationError({"copie_available": "Copies available cannot be negative."})
        
        serializer.save()

    def perform_destroy(self, instance):
        #restrict book deletion to admin users only
        if not self.request.user.is_staff:
            raise ValidationError({"detail": "Only admin users can delete books"})
        instance.delete()
