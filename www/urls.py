from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'www.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^maps/', include("maps.urls")),

    url(r'^demo', 'www.views.demo'),
    url(r'^demo/(?P<mp_name>[\w-]+)', 'www.views.demo'),
]
