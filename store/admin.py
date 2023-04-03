from django.contrib import admin
from .models import Artist, Concert, Ticket, Order, Cart, Town

admin.site.register(Artist)
admin.site.register(Concert)
admin.site.register(Ticket)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Town)
