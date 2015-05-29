from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets
from maps.serializers import MarkerSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from maps.models import Marker
from closet.models import Subcategory

from maps.models import Marker
from closet.models import Subcategory
from django.contrib.gis.geos import Point
import csv


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
    web = forms.URLField()
    phone = forms.CharField()
    adress = forms.CharField()
    lat = forms.FloatField(required=True)
    lon = forms.FloatField(required=True)
    description = forms.CharField()
    subcat = forms.CharField(validators=[validate_subcat])


class ImportForm(forms.Form):
    name = forms.CharField(required=True)
    csv = forms.CharField(required=True, widget=forms.Textarea)


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
                public=True,
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
            return HttpResponseBadRequest('Invalid form')

    return HttpResponseBadRequest('POST ONLY')


from closet.models import Category


@login_required
def importer(request):
    if request.method == 'POST':
        form = ImportForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cat = Category.objects.get(name=data['name'])
            im(data['csv'], cat)

            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest('Invalid form')

    else:
        form = ImportForm()

    return render(request, 'maps/importer.html', {'form': form})

from django.db import transaction
from io import StringIO


@transaction.non_atomic_requests
def im(data, AAA):
    mapping = {
        'name': "NOM",
        'lat': "LAT",
        'lon': "LONG",
        'comment': "DESCRIPTION",
        'rue': 'RUE',
        'code': 'CODE',
        'commune': 'COMMUNE',
        'web': 'WEBSITE',
        'phone': 'TEL',
        'category': 'CATEGORIE',
    }

    f = StringIO(data)
    reader = csv.reader(f, delimiter=",")
    lines = list(reader)

    head = lines.pop(0)

    mapping_col = {key: head.index(full_name.strip()) for key, full_name in mapping.items()}

    points = []

    for line in lines:
        point = {}
        for name, col in mapping_col.items():
            point[name] = line[col].strip()

        if '' not in (point['name'], point['lat'], point['lon']):
            points.append(point)

    for point in points:
        lat = point['lat']
        if lat[-4] == '.':
            lat = lat[:-4] + lat[-3:]
        lon = point['lon']
        if lon[-4] == '.':
            lon = lon[:-4] + lat[-3:]
        pos = Point(float(lon), float(lat))
        web = point['web']
        if not web.startswith("http"):
            web = "http://" + web
        m = Marker.objects.create(
            name=point['name'],
            position=pos,
            comment=point['comment'],
            web=web,
            phone=point['phone'],
            adress="{0[rue]} {0[code]} {0[commune]}".format(point),
        )

        for cat in point['category'].split(','):
            subcat, created = Subcategory.objects.get_or_create(name=cat.strip().capitalize(), category=AAA)
            m.subcategories.add(subcat)

        m.save()

    Subcategory.objects.filter(name="").delete()
