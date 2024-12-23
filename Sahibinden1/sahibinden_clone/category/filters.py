import django_filters
from category.models import Araba, Ev

class EvFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="fiyat", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="fiyat", lookup_expr='lte')
    min_metrekare = django_filters.NumberFilter(field_name="metrekare", lookup_expr='gte')
    max_metrekare = django_filters.NumberFilter(field_name="metrekare", lookup_expr='lte')
    isinma_tipi = django_filters.CharFilter(field_name="isinma_tipi", lookup_expr='iexact')

    class Meta:
        model = Ev
        fields = ['min_price', 'max_price', 'min_metrekare', 'max_metrekare', 'isinma_tipi']

class ArabaFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="fiyat", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="fiyat", lookup_expr='lte')
    marka = django_filters.CharFilter(field_name="marka", lookup_expr='iexact')
    yakit_turu = django_filters.CharFilter(field_name="yakit_turu", lookup_expr='iexact')
    min_yil = django_filters.NumberFilter(field_name="yil", lookup_expr='gte')
    max_yil = django_filters.NumberFilter(field_name="yil", lookup_expr='lte')

    class Meta:
        model = Araba
        fields = ['min_price', 'max_price', 'marka', 'yakit_turu', 'min_yil', 'max_yil']
