from django.conf.urls import url

urlpatterns = [
    url(r'^iframe/(?P<mp_name>[\w-]+)$', 'maps.views.view_map', name='view_map'),
    url(
        r'^markers/(?P<mp_name>[\w-]+)/(?P<tag>[\w-]+)$',
        'maps.views.map_markers',
        name='map_markers_tag'
    ),
    url(
        r'^markers/(?P<mp_name>[\w-]+)$',
        'maps.views.map_markers',
        name='map_markers'
    ),
]
