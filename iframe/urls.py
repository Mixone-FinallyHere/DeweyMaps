from django.conf.urls import url

import iframe.views

urlpatterns = [
    url(r'^(?P<pk>\d+)', iframe.views.FrameView.as_view()),
    url(r'^add', iframe.views.IframeFormView.as_view())
]
