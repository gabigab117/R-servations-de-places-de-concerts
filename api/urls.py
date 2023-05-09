from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import TicketViewset, UserViewset, ConcertViewset


router = DefaultRouter()
router.register('ticket', TicketViewset, basename="ticket")
router.register('shopper', UserViewset, basename="shopper")
router.register('concert', ConcertViewset, basename="concert")

app_name = "api"
urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path('token/', TokenObtainPairView.as_view(), name="token-obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('', include(router.urls)),

]
