from django.conf.urls import url

import iframe.views

urlpatterns = [
    url(r'^(?P<pk>\d+)', iframe.views.FrameView.as_view()),
    url(r'^add', iframe.views.add),
    url(r'^snippet/(?P<pk>\d+)', iframe.views.snippet, name="snippet"),
]
