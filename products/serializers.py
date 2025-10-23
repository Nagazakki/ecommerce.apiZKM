from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
def validate_price(self, value):
    if value <= 0:
        raise serializers.ValidationError("Price must be greater than zero.")
    return value
def validate_stock_quantity(self, value):
    if value < 0:
        raise serializers.ValidationError("Stock quantity cannot be negative.")
    return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'