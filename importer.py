from maps.models import Marker
from django.contrib.gis.geos import Point
import csv
import json


mapping = {
    'name': "NOM",
    'lat': "LAT",
    'lon': "LONG",
    'comment': "DESCRIPTION",
    'rue': 'RUE',
    'code': 'CODE',
    'commune': 'COMMUNE',
}

template = """
<h5>{name}</h5>
<p>{comment}</p>

<em>Adresse : {rue}, {code} {commune}</em>
"""

f = open('/home/nikita/Desktop/dewey.csv', 'r')
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
    comment = template.format(**point)
    Marker.objects.create(name=point['name'], comment=comment, position=pos, json_data=json.dumps(point))
