
#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from books_app.models import Book
from .models import Transaction
from .serializers import TransactionSerializer
# Create your views here.

class CheckoutBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        user = request.user
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book does not exist."}, status=status.HTTP_404_NOT_FOUND)

        if book.copies_available <= 0:
            return Response({"error": "No copies available for this book."}, status=status.HTTP_400_BAD_REQUEST)

        if Transaction.objects.filter(user=user, book=book, return_date__isnull=True).exists():
            return Response({"error": "You have already checked out this book."}, status=status.HTTP_400_BAD_REQUEST)

        book.copies_available -= 1
        book.save()

        transaction = Transaction.objects.create(user=user, book=book, checkout_date=now())
        serializer = TransactionSerializer(transaction)


        return Response({"message": "Book checked out successfully."}, status=status.HTTP_201_CREATED)


class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        user = request.user
        transaction = Transaction.objects.filter(user=user, book_id=book_id, return_date__isnull=True).first()

        if not transaction:
            return Response({"error": "No active checkout record found."}, status=status.HTTP_400_BAD_REQUEST)

        transaction.return_date = now()
        transaction.save()

        book = transaction.book
        book.copies_available += 1
        book.save()

        serializer = TransactionSerializer(transaction)

        return Response({"message": "Book returned successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
