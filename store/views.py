from django.shortcuts import render, get_object_or_404
from .models import Concert, Ticket


def index(request):
    concerts = Concert.objects.all()

    return render(request, "store/index.html", context={"concerts": concerts})


def concert_detail(request, slug):
    concert = get_object_or_404(Concert, slug=slug)
    return render(request, 'store/detail.html', context={"concert": concert})
