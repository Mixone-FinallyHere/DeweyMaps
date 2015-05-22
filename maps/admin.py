from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from maps.models import Marker


class MarkerAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Marker, MarkerAdmin)
