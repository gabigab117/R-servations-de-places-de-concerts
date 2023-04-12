import os
from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from accounts.models import Shopper
from .models import Concert, Cart, Order, Ticket
from project.settings import STRIPE_APIKEY
import stripe
import iso3166

stripe.api_key = STRIPE_APIKEY


def index(request):
    concerts = Concert.objects.all()

    return render(request, "store/index.html", context={"concerts": concerts})


def concert_detail(request, slug):
    concert: Concert = get_object_or_404(Concert, slug=slug)
    tickets = concert.ticket.all()
    return render(request, 'store/detail.html', context={"concert": concert, "tickets": tickets})


def add_to_cart(request, pk):
    user = request.user
    ticket: Ticket = Ticket.objects.get(pk=pk)

    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(ticket=ticket, ordered=False, user=user)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    ticket.count -= 1
    ticket.save()

    return redirect('index')


def cart(request):
    cart: Cart = request.user.cart

    orders = cart.orders.all()

    return render(request, 'store/cart.html', context={"cart": cart, "orders": orders})


def delete_cart(request):
    cart = request.user.cart
    cart.order_ko()
    return redirect("index")


def create_checkout_session(request):
    # récupérer le panier
    cart = request.user.cart

    # compréhension de liste line_items :
    line_items = [{"price": order.ticket.stripe_id,
                   "quantity": order.quantity} for order in cart.orders.all()]
    # voir la doc https://stripe.com/docs/payments/accept-a-payment
    # créer un objet de type Session
    # https://stripe.com/docs/api/checkout/sessions/create
    session = stripe.checkout.Session.create(
        locale="fr",
        # récupérer l'email utilisateur
        customer_email=request.user.email,
        # récupérer l'adresse utilisateur
        shipping_address_collection={"allowed_countries": ["FR"]},
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri(reverse('store:success')),
        cancel_url='http://127.0.0.1:8000',
    )

    return redirect(session.url, code=303)


# créer une vue pour dire que la commande est payée
def checkout_success(request):
    return render(request, "store/success.html")


# https://stripe.com/docs/webhooks?locale=fr-CA
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = os.getenv('endpoint_secret')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # j'ai tout copié tel quel en supprimant les vérifications défaut.
    # je crée ma vérif :
    # https://stripe.com/docs/api/events
    if event['type'] == 'checkout.session.completed':
        data = event['data']['object']
        # récupérer l'utilisateur
        try:
            user: Shopper = get_object_or_404(Shopper, email=data['customer_details']['email'])

        except KeyError:
            return HttpResponse("invalid user email", status=404)
        # --^^-- appel de mes fonctions
        complete_order(data=data, user=user)
        save_shipping_address(data=data, user=user)
        return HttpResponse(status=200)

    return HttpResponse(status=200)


def complete_order(data, user):
    user.stripe_id = data["customer"]
    user.cart.order_ok()
    user.save()

    return HttpResponse(status=200)


def save_shipping_address(data, user):
    pass
