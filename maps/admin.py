from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from maps.models import Marker


class MarkerAdmin(LeafletGeoAdmin):
    list_display = ('name', 'web', 'phone', 'adress', 'public')
    list_filter = ('public', 'subcategories', 'created')
    search_fields = ('name', 'comment', 'web')

admin.site.register(Marker, MarkerAdmin)
