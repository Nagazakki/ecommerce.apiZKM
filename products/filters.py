import django_filters
from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    in_stock = filters.BooleanFilter(method='filter_in_stock')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'in_stock']

    def filter_in_stock(self, queryset, name, value):
        if value is True:
            return queryset.filter(stock_quantity__gt=0)
        if value is False:
            return queryset.filter(stock_quantity__lte=0)
        return queryset