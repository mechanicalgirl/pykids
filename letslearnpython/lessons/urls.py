from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lesson/(?P<lesson_number>[0-9]+)/step/(?P<step_number>[0-9]+)/$', views.lesson_step, name='lesson_step_detail'),
    url(r'^lesson/(?P<lesson_number>[0-9]+)/$', views.lesson, name='lesson'),
]
