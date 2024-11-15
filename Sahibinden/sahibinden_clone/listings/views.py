from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing
from .serializers import ListingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    # Filtreleme ve sıralama backend'lerini etkinleştir
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'category': ['exact'],  # Emlak veya Araba filtrelemesi
        'price': ['gte', 'lte'],  # Fiyat aralığı
        'location': ['icontains'],  # Konum arama
        'rooms': ['gte', 'lte'],  # Oda sayısı (sadece emlak)
        'area': ['gte', 'lte'],  # Metrekare (sadece emlak)
        'make': ['exact'],  # Marka (sadece araba)
        'year': ['gte', 'lte'],  # Model yılı (sadece araba)
        'mileage': ['gte', 'lte'],  # Kilometre (sadece araba)
    }
    ordering_fields = ['price', 'created_at']  # Fiyat veya oluşturulma tarihi sırasına göre
