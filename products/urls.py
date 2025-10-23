from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = router.urls