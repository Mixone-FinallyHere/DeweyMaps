from iframe.models import Map
from django.views.generic.detail import DetailView
from django.views.generic import FormView

from iframe.serializers import MapSerializer
from rest_framework import viewsets
from iframe.forms import MapForm

from django.views.decorators.clickjacking import xframe_options_exempt


class FrameView(DetailView):
    model = Map
    context_object_name = 'map'

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        return super(DetailView, self).get(request, *args, **kwargs)


class IframeViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class IframeFormView(FormView):
    form_class = MapForm
    template_name = "iframe/map_form.html"
