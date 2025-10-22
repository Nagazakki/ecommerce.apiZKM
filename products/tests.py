from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product

class ProductAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass1234")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.url = '/api/products/'

    def test_create_product(self):
        data = {
            "name": "Test Product",
            "description": "A sample product for testing",
            "price": 50.00,
            "category": "Accessories",
            "stock_quantity": 10,
            "image_url": "https://example.com/image.jpg",
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "Test Product")