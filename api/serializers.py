from store.models import Ticket, Concert
from accounts.models import Shopper
from rest_framework import serializers


class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        depth = 1


class ShopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopper
        fields = ['first_name']
