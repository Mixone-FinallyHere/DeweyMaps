from iframe.models import Map
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.gis.geos import Point
from django.core.urlresolvers import reverse

from iframe.serializers import MapSerializer
from rest_framework import viewsets
from iframe.forms import MapForm
from closet.models import Category


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


def add(request):
    if request.method == 'POST':
        form = MapForm(request.POST)
        if form.is_valid():
            frame = Map.objects.create(
                zoom=form.cleaned_data['zoom'],
                center=Point(form.cleaned_data['longitude'], form.cleaned_data['latitude']),
            )
            frame.subcategories.add(*form.cleaned_data['subcategories'])
            return HttpResponseRedirect(reverse('snippet', args=[frame.id]))
    else:
        form = MapForm() # An unbound form

    return render(request, 'iframe/map_form.html', {
        'form': form,
        'categories': Category.objects.all(),
    })


def snippet(request, pk):
    return render(request, 'iframe/snippet.html', {
        'id': pk,
    })
