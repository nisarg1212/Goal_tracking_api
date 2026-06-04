from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserRegistrationView

urlpatterns = [
    # User Registration Endpoint
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    
    # JWT Auth Endpoints
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refersh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
