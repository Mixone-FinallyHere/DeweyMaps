from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from maps.serializers import MapSerializer, MarkerSerializer

from maps.models import Map, Marker


def view_map(request, mp_id):
    mp = get_object_or_404(Map, id=mp_id)

    markers_tags = map(lambda x: set(x.tags.all()), mp.markers.all())
    tags = set()
    for marker_tags in markers_tags:
        tags.update(marker_tags)

    context = {
        'map': mp,
        'tags': tags,
    }

    return render(request, 'maps/embed.html', context)


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
