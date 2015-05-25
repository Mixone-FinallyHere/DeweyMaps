from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets
from maps.serializers import MarkerSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point
from django import forms


from maps.models import Marker
from closet.models import Subcategory


def validate_subcat(input):
    sub = input.split(",")
    # if len(sub) < 1:
    #     raise ValidationError("Il faut au moins sélectionner une sous-catégorie")
    for cat in sub:
        if not cat.isnumeric():
            ValidationError("Catégorie invalide")


class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.prefetch_related('subcategories').filter(public=True)
    serializer_class = MarkerSerializer


class MarkerForm(forms.Form):
    name = forms.CharField(required=True)
    web = forms.URLField(required=False)
    phone = forms.CharField(required=False)
    adress = forms.CharField(required=False)
    lat = forms.FloatField(required=True)
    lon = forms.FloatField(required=True)
    description = forms.CharField(required=False)
    subcat = forms.CharField(validators=[validate_subcat], required=False)


@csrf_exempt
def add_marker(request):
    if request.method == 'POST':
        form = MarkerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            m = Marker.objects.create(
                name=data['name'],
                web=data['web'],
                phone=data['phone'],
                adress=data['adress'],
                position=Point(data['lon'], data['lat']),
                comment=data['description'],
                public=False,
            )

            for sub in data['subcat'].strip().split(','):
                sub = sub.strip()
                if sub.isnumeric():
                    sub = int(sub)
                    sub = Subcategory.objects.get(id=sub)
                    m.subcategories.add(sub)

            m.save()

            return HttpResponse(m.id)
        else:
            import ipdb; ipdb.set_trace()
            return HttpResponseBadRequest('Invalid form')

    return HttpResponseBadRequest('POST ONLY')
