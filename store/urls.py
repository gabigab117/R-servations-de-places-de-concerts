from django.urls import path
from .views import concert_detail, add_to_cart, cart, delete_cart, create_checkout_session, checkout_success, stripe_webhook


app_name = "store"
urlpatterns = [
    path("concert/<str:slug>", concert_detail, name="concert-detail"),
    path('add-to-cart/ticket/<int:pk>/', add_to_cart, name="add-to-cart"),
    path('stripe-webhook/', stripe_webhook, name='stripe-webhook'),
    path('cart/', cart, name='cart'),
    path('cart/create-checkout-session/', create_checkout_session, name="create-checkout-session"),
    path('cart/success/', checkout_success, name="success"),
    path('delete_cart/', delete_cart, name="delete-cart"),
    ]
