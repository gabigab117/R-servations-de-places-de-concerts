from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewset, UserViewset


router = DefaultRouter()
router.register('ticket', TicketViewset)
router.register('shopper', UserViewset)


urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path('', include(router.urls)),

]
