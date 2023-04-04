from django.urls import path
from .views import concert_detail


app_name = "store"
urlpatterns = [
    path("concert/<str:slug>", concert_detail, name="concert-detail")
    ]
