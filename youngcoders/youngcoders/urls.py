from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  ## main youngcoder views
    url(r'^learn/', include('lessons.urls')),
    url(r'^teach/', include('teaching.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
]
