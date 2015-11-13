from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from iframe.models import Map


class MapAdmin(LeafletGeoAdmin):
    list_display = ('name', 'uuid')
    search_fields = ('name', )

admin.site.register(Map, MapAdmin)
