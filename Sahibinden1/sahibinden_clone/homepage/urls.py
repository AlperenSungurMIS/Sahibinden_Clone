from django.urls import path
from .views import ListingAPIView

urlpatterns = [
    path('', ListingAPIView.as_view(), name='api-listings'),  # İlanları listeleme ve ekleme endpoint'i
    path('listings/', ListingAPIView.as_view(), name='api-listings'),
]
