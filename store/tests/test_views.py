from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import Shopper
from store.models import Artist, Town, Ticket, Concert


class StoreTest(TestCase):
    def setUp(self):
        gojira = Artist.objects.create(name="Gojira")
        bvs = Town.objects.create(name="beauvais")

        self.ticket = Ticket.objects.create(
            name="ticket A",
            stock=1,
            artist=gojira,
            city=bvs,
            country="fr",
            date=timezone.now()
        )

        self.ticket2 = Ticket.objects.create(
            name="ticket A",
            stock=0,
            artist=gojira,
            city=bvs,
            country="fr",
            date=timezone.now()
        )

        self.user: Shopper = Shopper.objects.create(
            email="gabrieltrouve5@gmail.com",
            password="12345678",
            first_name="Trouve",
            last_name="gabriel"
        )

        self.concert = Concert.objects.create(
            name=gojira,
            type="metal",
            place="salle",
            city=bvs,
            date=timezone.now()
        )

    def test_product_are_shown_on_index_if_stock(self):
        self.concert.ticket.add(self.ticket)
        resp = self.client.get(reverse('index'))
        # self.assertEqual(resp.status_code, 200)
        # resp.content contenu de la page HTML
        self.assertIn(self.concert.name.name, str(resp.content))

    def test_product_are_shown_on_index_if_not_stock(self):
        self.concert.ticket.add(self.ticket2)
        resp = self.client.get(reverse('index'))
        # self.assertEqual(resp.status_code, 200)
        # resp.content contenu de la page HTML
        self.assertIn(self.concert.name.name, str(resp.content))

    def test_connexion_link_shown_when_not_connected(self):
        resp = self.client.get(reverse('index'))
        self.assertIn("Connexion", str(resp.content))

    def test_redirect_when_anonymous_user_access_cart_view(self):
        resp = self.client.get(reverse('store:cart'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, f"{reverse('account:login')}?next={reverse('store:cart')}")
