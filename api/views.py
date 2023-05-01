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


class UserViewset(viewsets.ModelViewSet):
    queryset = Shopper.objects.all()
    serializer_class = ShopperSerializer

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
