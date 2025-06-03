from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterViewTest(TestCase):
    def setUp(self):
        # Ajustamos el nombre de la URL con namespace 'users'
        self.url = reverse("users:register")

    def test_get_returns_200_and_uses_correct_template(self):
        """
        Upon making a GET request to the registration view:
        - It should respond with status 200.
        - It should use the 'registration/register.html' template.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
