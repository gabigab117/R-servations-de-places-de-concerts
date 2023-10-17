import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from accounts.models import Shopper, ShippingAddress
from .models import Concert, Order
from project.settings import STRIPE_APIKEY
import stripe
from django.forms import modelformset_factory
from store.forms import OrderForm

stripe.api_key = STRIPE_APIKEY


def index(request):
    concerts = Concert.objects.all()

    if request.method == "GET":
        name = request.GET.get('recherche')
        if name:
            concerts = Concert.objects.filter(slug__icontains=name)

    return render(request, "store/index.html", context={"concerts": concerts})


def concert_detail(request, slug):
    # concert: Concert = get_object_or_404(Concert, slug=slug)
    concert: Concert = Concert.objects.get(slug=slug)
    tickets = concert.ticket.all()
    return render(request, 'store/detail.html', context={"concert": concert, "tickets": tickets})


def add_to_cart(request, pk):
    user: Shopper = request.user
    user.add_to_cart(pk=pk)

    return redirect('index')


@login_required
def cart(request):
    user = request.user
    cart = user.cart
    total_orders = Order.total(user=user)
    orders = cart.orders.all()

    # https://docs.djangoproject.com/fr/4.1/ref/forms/models/
    # créer une classe depuis modelformset_factory
    OrderFormSet = modelformset_factory(Order, form=OrderForm, extra=0)
    # puis créer une instance
    formset = OrderFormSet(queryset=orders)

    if request.method == "POST":
        formset = OrderFormSet(request.POST, queryset=orders)
        if formset.is_valid():
            formset.save()
            if orders.count() == 0:
                cart.delete()
                return redirect('index')
            return redirect('store:cart')

    return render(request, 'store/cart.html', context={"forms": formset,
                                                       "user": user, "total": total_orders})


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
    checkout_data = {
        "locale": "fr",
        "line_items": line_items,
        "mode": 'payment',
        # voir ds la doc. On passe un dico avec une liste de pays autorisés
        "shipping_address_collection": {"allowed_countries": ["FR", "BE"]},
        # il faut une url absolue car je suis sur Stripe à ce moment-là
        "success_url": request.build_absolute_uri(reverse('store:success')),
        "cancel_url": 'http://127.0.0.1:8000',
    }
    if request.user.stripe_id:
        checkout_data["customer"] = request.user.stripe_id
    else:
        checkout_data["customer_email"] = request.user.email
        checkout_data["customer_creation"] = "always"

    session = stripe.checkout.Session.create(**checkout_data)

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


# enregistrer l'adresse stripe dans ma BDD
def save_shipping_address(data, user):
    """
       "shipping_details": {
        "address": {
          "city": "60650 - ONS EN BRAY",
          "country": "FR",
          "line1": "5 rue xxxxxx",
          "line2": null,
          "postal_code": "60650",
          "state": ""
        },
        "name": "GABRIEL TROUV\u00c9"
        """
    try:
        address = data["shipping_details"]["address"]
        name = data["shipping_details"]["name"]
        city = address["city"]
        country = address["country"]
        line1 = address["line1"]
        line2 = address["line2"]
        zip_code = address["postal_code"]
        state = address["state"]
    except KeyError:
        return HttpResponse(status=400)
    # potentiellement l'adresse peut exister
    ShippingAddress.objects.get_or_create(user=user,
                                          name=name,
                                          city=city,
                                          country=country.lower(),
                                          address_1=line1,
                                          address_2=line2 or "",
                                          zip_code=zip_code)
    return HttpResponse(status=200)


