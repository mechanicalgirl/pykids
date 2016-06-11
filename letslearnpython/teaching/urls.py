from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^step/(?P<step_number>[0-9]+)/$', views.step, name='step_detail'),
]
