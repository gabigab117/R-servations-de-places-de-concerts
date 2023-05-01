from django.test import TestCase
from store.models import Ticket, Artist, Town, Cart, Order
from accounts.models import Shopper
from django.utils import timezone


class Test(TestCase):
    # méthode setUp qui sera lancée automatiquement
    def test_order_ko(self):
        gojira = Artist.objects.create(name="gojira")
        bvs = Town.objects.create(name="beauvais")
        user = Shopper.objects.create(
            email="gabrieltrouve5@gmail.com",
            password="12345678",
            first_name="Trouve",
            last_name="gabriel"
        )

        self.instance_of_ticket = Ticket.objects.create(
            name="Ticket A",
            price=10,
            stock=10,
            artist=gojira,
            city=bvs,
            country="France",
            date=timezone.now()
        )
        self.cart = Cart.objects.create(user=user)
        order = Order.objects.create(
            ticket=self.instance_of_ticket,
            user=user
        )
        self.cart.orders.add(order)
        self.cart.save()

        self.cart.order_ko()
        self.assertTrue(order.ordered)
