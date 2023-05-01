from store.models import Ticket
from accounts.models import Shopper
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        depth = 1


class ShopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopper
        fields = "__all__"
