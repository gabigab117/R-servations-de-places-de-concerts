from store.models import Ticket, Concert
from accounts.models import Shopper
from rest_framework import viewsets
from .serializers import TicketSerializer, ShopperSerializer, ConcertSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminAuthenticated


class ConcertViewset(viewsets.ModelViewSet):
    serializer_class = ConcertSerializer
    queryset = Concert.objects.all()


class TicketViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = {"price": ["gte", "lte"],
                        "id": ["in"]}


class UserViewset(viewsets.ModelViewSet):
    # queryset = Shopper.objects.all()
    serializer_class = ShopperSerializer
    # être connecté pour accéder :
    permission_classes = [IsAdminAuthenticated]

    # je peux utiliser la méthode get_queryset
    def get_queryset(self):
        queryset = Shopper.objects.filter(is_active=True)
        # si je veux filtrer par l'url genre :
        # http://127.0.0.1:8000/api/shopper/?email=gabrieltrouve5@gmail.com
        # "email" sera donc le paramètre de l'url
        email = self.request.GET.get("email")
        if email:
            queryset = Shopper.objects.filter(email=email)
        return queryset

    '''
    fieldset = {
                field.name: [
                    "exact",
                    "gt",
                    "gte",
                    "lt",
                    "lte",
                    "in",
                    "iexact",
                    "startswith",
                    "istartswith",
                    "endswith",
                    "iendswith",
                    "regex",
                    "iregex",
                    "isnull",
                    "contains",
                    "icontains",
                    "ne",
                ]
    '''
