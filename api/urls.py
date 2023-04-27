from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewset


router = DefaultRouter()
router.register('ticket', TicketViewset)


urlpatterns = [
    path('', include(router.urls)),

]
