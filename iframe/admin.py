from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from iframe.models import Map


class MapAdmin(LeafletGeoAdmin):
    # list_display = ('name', 'web', 'phone', 'adress', 'public')
    # list_filter = ('public', 'subcategories', 'created')
    # search_fields = ('name', 'comment', 'web')
    pass

admin.site.register(Map, MapAdmin)
