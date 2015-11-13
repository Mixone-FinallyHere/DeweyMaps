from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from www import settings

import maps.views
import closet.views
import iframe.views

router = routers.DefaultRouter()
router.register(r'markers', maps.views.MarkerViewSet)
router.register(r'categories', closet.views.CategoryViewSet)
router.register(r'iframes', iframe.views.IframeViewSet)

urlpatterns = [
    url(r'^$', 'www.views.index'),
    url(r'^add/$', 'maps.views.importer'),
    url(r'^addmarker$', 'maps.views.add_marker'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^frame/(?P<pk>\d+)', iframe.views.FrameView.as_view()),
]

if settings.DEBUG:
    from django.contrib.staticfiles import views
    urlpatterns += [url(r'^static/(?P<path>.*)$', views.serve)]
