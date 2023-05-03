from store.models import Ticket
from accounts.models import Shopper
from rest_framework import viewsets
from .serializers import TicketSerializer, ShopperSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class TicketViewset(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = {"price": ["gte", "lte"],
                        "id": ["in"]}


class UserViewset(viewsets.ReadOnlyModelViewSet):
    # queryset = Shopper.objects.all()
    serializer_class = ShopperSerializer

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
