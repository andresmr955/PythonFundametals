from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterViewTest(TestCase):
    def setUp(self):
        # Ajustamos el nombre de la URL con namespace 'users'
        self.url = reverse('users:register')

    def test_get_returns_200_and_uses_correct_template(self):
        """
        Al hacer GET a la vista de registro:
        - Debe responder con status 200.
        - Debe usar el template 'registration/register.html'.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')