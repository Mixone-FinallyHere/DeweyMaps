from maps.models import Map, Marker
from django.contrib.gis.geos import Point

mp = Map.objects.get(id=id)

mapping = {
    'name': "Nom",
    'lat': "Latitude",
    'lon': "Longitude",
    'comment': "Description"
}

f = open('/home/nikita/Carte_assocs_fini.csv', 'r')
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
    pos = Point(float(point['lon']), float(point['lat']))
    mp.markers.create(name=point['name'], comment=point['comment'], position=pos)
