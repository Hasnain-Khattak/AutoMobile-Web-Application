import django_filters
from .models import Listing

class ListingFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', label='Min Price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', label='Max Price', lookup_expr='lte')
    model = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Listing
        fields = ['brand', 'model', 'min_price', 'max_price']