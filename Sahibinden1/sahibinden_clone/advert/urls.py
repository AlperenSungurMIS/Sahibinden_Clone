from django.urls import path
from .views import AdvertDetailAPIView

urlpatterns = [
    path('<int:pk>/', AdvertDetailAPIView.as_view(), name='advert-detail'),
]