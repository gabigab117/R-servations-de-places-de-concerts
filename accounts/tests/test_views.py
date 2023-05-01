from django.test import TestCase

from django.urls import reverse

from accounts.models import Shopper


class StoreLoggedInTest(TestCase):
    def setUp(self):
        self.user = Shopper.objects.create_user(
            email="gabrieltrouve@gmail.com",
            first_name="Trouve",
            last_name="gabriel",
            password="123456789"
        )

    def test_valid_login(self):
        data = {'username': 'gabrieltrouve@gmail.com', 'password': '123456789'}
        resp = self.client.post(reverse('account:login'), data=data)
        self.assertEqual(resp.status_code, 302)
        resp = self.client.get(reverse('index'))
        self.assertIn("Profile", str(resp.content))

    def test_invalid_login(self):
        data = {'username': 'gabrieltrouve@gmail.com', 'password': '1234'}
        resp = self.client.post(reverse('account:login'), data=data)
        self.assertEqual(resp.status_code, 200)

    def test_profile_change(self):
        # je connecte l'utilisateur
        self.client.login(email="gabrieltrouve@gmail.com", password="123456789")
        data = {
            "email": "gabrieltrouve@gmail.com",
            "password": "123456789",
            "genre": "f",
            "last_name": "ouioui",
            "first_name": "gaga",
            "tel": "0344805112"
        }
        resp = self.client.post(reverse("account:profil"), data=data)
        self.assertEqual(resp.status_code, 302)
        gab: Shopper = Shopper.objects.get(email='gabrieltrouve@gmail.com')
        self.assertEqual(gab.last_name, "ouioui")
