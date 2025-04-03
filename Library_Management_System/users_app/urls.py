from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy, UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
