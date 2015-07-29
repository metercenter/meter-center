from django.conf.urls import patterns, url

from datahandle import views

urlpatterns = patterns('',
    url(r'^$', views.display, name='display'),
)
