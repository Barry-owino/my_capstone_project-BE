from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from books_app.models import Book

# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transactions')
    checkout_date = models.DateTimeField(default=now)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'book', 'is_returned') #prevents multiple active checkouts

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

    def save(self, *args, **kwargs):
        if self.return_date and self.return_date < self.checkout_date:
            raise ValueError("Return date cannot be before the checkout date.")
        super().save(*args, **kwargs)
