from django.shortcuts import render, get_object_or_404

from maps.models import Map


def demo(request, mp_name="Villo"):
    mp = get_object_or_404(Map, name=mp_name)

    return render(request, 'www/demo.html', {'map_name': mp.name})
