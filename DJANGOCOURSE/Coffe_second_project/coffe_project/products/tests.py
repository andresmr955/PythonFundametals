from django.test import TestCase
from django.urls import reverse
from .models import Product

# Create your tests here.

# class ProductListTest(TestCase):

#     def test_should_return_200(self):
#         url = reverse('product_list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#     def test_should_return_200_with_products(self):
#         url = reverse('product_list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.context['products'].count(), 0)
