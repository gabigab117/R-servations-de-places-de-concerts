from store.models import Ticket
from rest_framework import viewsets
from .serializers import TicketSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class TicketViewset(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = {"price": ["gte", "lte"],
                        "id": ["in"]}

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
