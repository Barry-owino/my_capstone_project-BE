from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from books_app.models import Book

# Create your models here.

class BookCheckout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(default=now)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
