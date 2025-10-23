from django.shortcuts import render
from rest_framework import viewsets, permissions, filters as drf_filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .filters import ProductFilter
from products import filters

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'category', 'description']
    ordering_fields = ['price', 'created_at', 'stock_quantity']
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_fields = {
        'category': ['exact'],
        'price': ['gte', 'lte'],
        'stock_quantity': ['gte', 'lte'],
    }
    search_fields = ['name', 'category']
    ordering_fields = ['price', 'created_at', 'stock_quantity']
    ordering = ['-created_at']

    def get_permissions(self):
        # Allow read-only access to everyone, but restrict modification to authenticated users
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
            return [p() for p in permission_classes]
        else:
            permission_classes = [permissions.IsAuthenticated]  
        return [permission() for permission in permission_classes]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        # Allow read-only access to everyone, but restrict modification to authenticated users
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
            return [p() for p in permission_classes]
        else:
            permission_classes = [permissions.IsAuthenticated]  
        return [permission() for permission in permission_classes]