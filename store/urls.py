from django.urls import path
from .views import concert_detail, add_to_cart


app_name = "store"
urlpatterns = [
    path("concert/<str:slug>", concert_detail, name="concert-detail"),
    path('add-to-cart/<str:slug>/<str:pk>/', add_to_cart, name="add-to-cart")
    ]
