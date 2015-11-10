from django.shortcuts import render
from iframe.models import Map
from iframe.serializers import MapSerializer
from rest_framework import viewsets


def frame(request, pk):
    frame = Map.objects.get(pk=pk)
    return render(request, 'iframe/frame.html', {'frame': frame})


class IframeViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
