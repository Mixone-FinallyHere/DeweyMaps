from iframe.models import Map
from django.views.generic.detail import DetailView
from iframe.serializers import MapSerializer
from rest_framework import viewsets


class FrameView(DetailView):
    model = Map
    context_object_name = 'map'


class IframeViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
