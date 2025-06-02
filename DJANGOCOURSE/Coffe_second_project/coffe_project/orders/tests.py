from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import Http404

from .views import CreateOrderView
from .models import Product, Order, OrderProduct


# class MyOrderViewTest(TestCase):

#     def test_no_logged_user_should_redirect(self):
#         url = reverse('my_order')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 302)  # 302 es el código para redirect

#     def test_logged_user_access_my_order(self):
#         User = get_user_model()
#         user = User.objects.create(username="testuser")
#         self.client.force_login(user)
        
#         url = reverse('my_order')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)



