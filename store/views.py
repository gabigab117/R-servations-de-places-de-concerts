from django.shortcuts import render
from .models import Concert


def index(request):
    concerts = Concert.objects.all()

    return render(request, "store/index.html", context={"concerts": concerts})
