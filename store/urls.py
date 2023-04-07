from django.urls import path
from .views import concert_detail, add_to_cart, cart, delete_cart


app_name = "store"
urlpatterns = [
    path("concert/<str:slug>", concert_detail, name="concert-detail"),
    path('add-to-cart/<str:slug>/<int:pk>/', add_to_cart, name="add-to-cart"),
    path('cart/', cart, name='cart'),
    path('delete_cart/', delete_cart, name="delete-cart"),
    ]
