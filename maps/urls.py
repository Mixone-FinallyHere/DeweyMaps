from django.conf.urls import url

urlpatterns = [
    url(r'^iframe/(?P<mp_id>[\w-]+)$', 'maps.views.view_map', name='view_map'),
]
