from django.shortcuts import render, get_object_or_404, redirect
from .models import Concert, Cart, Order


def index(request):
    concerts = Concert.objects.all()

    return render(request, "store/index.html", context={"concerts": concerts})


def concert_detail(request, slug):
    concert = get_object_or_404(Concert, slug=slug)
    return render(request, 'store/detail.html', context={"concert": concert})


def add_to_cart(request, slug, pk):
    user = request.user
    concert: Concert = get_object_or_404(Concert, slug=slug)
    ticket = concert.ticket.get(artist=concert.name, city=concert.city, pk=pk)

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
    cart.delete()
    return redirect("index")
