
#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from books_app.models import Book
from .models import BookCheckout

# Create your views here.

class CheckoutBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        user = request.user
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not exist."}, status=status.HTTP_404_NOT_FOUND)

        if book.copies_available <= 0:
            return Response({"error": "No copies available for this book."}, status=status.HTTP_400_BAD_REQUEST)

        if BookCheckout.objects.filter(user=user, book=book, return_date__isnull=True).exist():
            return Response({"error": "You have already checked out this book."}, status=status.HTTP_400_BAD_REQUEST)

        book.available_copies -=1
        book.save()

        BookCheckout.objects.create(user=user, book=book, checkout_date=now())

        return Response({"mesaage": "Book checked out successfully."}, status=status.HTTP_200_OK)


class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        user = request.user
        checkout = BookCheckout.objects.filter(user=user, book_id=book_id, return_date__isnull=True).first()

        if not checkout:
            return Response({"error": "No active checkout record found."}, status=status.HTTP_400_BAD_REQUEST)

        checkout.return_date = now()
        checkout.save()

        book = checkout.book
        book.available_copies += 1
        book.save()

        return Response({"message": "Book returned successfully."}, status=status.HTTP_200_OK)
