from rest_framework.test import APITestCase
from django.urls import reverse_lazy
from accounts.models import Shopper


class TestShopper(APITestCase):
    # list est la complétude faite par le routeur
    url = reverse_lazy('api:shopper-list')

    def test_shopper_not_shown_if_not_isactive(self):
        user: Shopper = Shopper.objects.create_user(email="denine@denine.com",
                                                    genre="nr",
                                                    first_name="Denis",
                                                    last_name="Noone",
                                                    password="123456789",
                                                    is_active=False)

        user_2: Shopper = Shopper.objects.create_user(email="denine2@denine.com",
                                                      genre="nr",
                                                      first_name="Denis",
                                                      last_name="Noone",
                                                      password="123456789",
                                                      is_active=True)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(user.email, str(response.content))
        self.assertIn(user_2.email, str(response.content))
