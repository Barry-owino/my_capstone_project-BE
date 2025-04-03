from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy, UserLoginView

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
    path('login/', UserLoginView.as_view(), name='login'),
]
