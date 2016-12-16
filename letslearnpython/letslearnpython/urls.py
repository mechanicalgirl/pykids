from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

from . import views

urlpatterns = [
    url(r'^learn/',   include('lessons.urls')),
    url(r'^teach/',   include('teaching.urls')),
    url(r'^page/',    include('pages.urls')),
    url(r'^contact/', views.contactus, name='contact'),
    url(r'^landing/', include('landing_app.urls')),
    url(r'^admin/',   include(admin.site.urls)),
    url(r'^favicon\.ico$',  RedirectView.as_view(url='/static/letslearnpython/images/favicon.ico')),
    url(r'^$',        views.index, name='index'),
]
