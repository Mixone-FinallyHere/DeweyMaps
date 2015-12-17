from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from iframe.models import Map


class MapAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Map, MapAdmin)
