from django.urls import path
from .views import RegisterAPIView, RepasswordAPIView, LogoutAPIView, LoginAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api-register'),  # Register endpoint
    path('re-password/', RepasswordAPIView.as_view(), name='api-repassword'),  # Password reset endpoint
    path('logout/', LogoutAPIView.as_view(), name='api-logout'),  # Logout endpoint
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Token oluşturma endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token yenileme endpoint
    path('login/', LoginAPIView.as_view(), name='login'),  # Giriş yap endpoint
]
