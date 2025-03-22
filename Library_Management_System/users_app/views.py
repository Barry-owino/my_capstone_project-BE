#from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializers import UserSerializer

# Create your views here.
class UserListCreate(generics.ListCreateAPIView):
    queryst = Users.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
