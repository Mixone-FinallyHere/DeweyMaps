from maps.models import Marker
from closet.models import Subcategory
from django.contrib.gis.geos import Point
import csv

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


f = open("/home/nikita/Downloads/CARTE DEWEY & REPAIR TOGETHER - 1 - RECUP' - HABI-ENER.csv", 'r')
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
    m = Marker.objects.create(
        name=point['name'],
        position=pos,
        comment=point['comment'],
        web=point['web'],
        phone=point['phone'],
        adress="{0[rue]} {0[code]} {0[commune]}".format(point),
    )

    for cat in point['category'].split(','):
        subcat, created = Subcategory.objects.get_or_create(name=cat.strip().capitalize())
        m.subcategories.add(subcat)

    m.save()
