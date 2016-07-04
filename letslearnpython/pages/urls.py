from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<page_name>[a-z]+)/$', views.index, name='page_detail'),
]
