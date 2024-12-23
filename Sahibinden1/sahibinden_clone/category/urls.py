from django.urls import path
from .views import ArabaAPIView, EvAPIView

urlpatterns = [
    path('araba/', ArabaAPIView.as_view(), name='api-araba'),
    path('araba/<int:pk>/', ArabaAPIView.as_view(), name='api-araba-detail'),
    path('ev/', EvAPIView.as_view(), name='api-ev'),
    path('ev/<int:pk>/', EvAPIView.as_view(), name='api-ev-detail'),
    

]
