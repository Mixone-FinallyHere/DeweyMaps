from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from maps.models import Map, Marker


class MapAdmin(LeafletGeoAdmin):
    pass


class MarkerAdmin(LeafletGeoAdmin):
    pass


admin.site.register(Map, MapAdmin)
admin.site.register(Marker, MarkerAdmin)
