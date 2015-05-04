from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from maps import views

router = routers.DefaultRouter()
router.register(r'maps', views.MapViewSet)
router.register(r'markers', views.MarkerViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo', 'www.views.demo'),
    url(r'^demo/(?P<mp_id>[\w-]+)', 'www.views.demo'),
    url(r'^api/', include(router.urls)),
    url(r'^embed/', include('maps.urls')),
]
