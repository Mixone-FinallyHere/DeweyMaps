from django.shortcuts import render, get_object_or_404

from maps.models import Map


def demo(request, mp_id=1):
    mp = get_object_or_404(Map, id=mp_id)

    return render(request, 'www/demo.html', {'map': mp})


def index(request):
    return render(request, 'www/index.html')
