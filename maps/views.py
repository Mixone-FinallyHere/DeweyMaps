from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from maps.models import Map, Marker


def view_map(request, mp_name):
    mp = get_object_or_404(Map, name=mp_name)

    markers_tags = map(lambda x: set(x.tags.all()), mp.marker_set.all())
    tags = set()
    for marker_tags in markers_tags:
        tags.update(marker_tags)

    context = {
        'map': mp,
        'tags': tags,
    }

    return render(request, 'maps/map.html', context)


def map_markers(request, mp_name, tag=None):
    print(mp_name)
    mp = get_object_or_404(Map, name=mp_name)
    markers = Marker.objects.filter(map=mp)
    if tag is not None:
        markers = markers.filter(tags__slug=tag)
    context = {
        'markers': list(map(lambda x: x.jsonable(), markers))
    }

    return JsonResponse(context)
