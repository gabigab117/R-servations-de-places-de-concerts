from django.test import TestCase
from django.utils import timezone

from accounts.models import Shopper
from store.models import Ticket, Artist, Town


class UserTest(TestCase):
    def setUp(self):
        gojira = Artist.objects.create(name="gojira")
        bvs = Town.objects.create(name="beauvais")
        self.user: Shopper = Shopper.objects.create(
            email="gabrieltrouve5@gmail.com",
            password="12345678",
            first_name="Trouve",
            last_name="gabriel"
        )

        Ticket.objects.create(
            name="Ticket A",
            price=10,
            stock=10,
            artist=gojira,
            city=bvs,
            country="France",
            date=timezone.now()
        )

    def test_add_to_cart(self):
        self.user.add_to_cart(pk=1)
        self.assertEqual(self.user.cart.orders.count(), 2)

    def test_add_to_cart_quantity(self):
        self.user.add_to_cart(pk=1)
        self.user.add_to_cart(pk=1)
        quantity = self.user.cart.orders.get(pk=1)
        self.assertEqual(quantity.quantity, 3)
