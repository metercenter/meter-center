from django.conf.urls import patterns, include, url
from django.contrib import admin
from MeterManagment.views import mainPage
from MeterManagment.views import getMeter
from MeterManagment.views import userList
from MeterManagment.views import getData
from MeterManagment.views import loginPage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Measuringsystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get-meter', getMeter),
    url(r'^Users/List', userList),
    url(r'^get-data', getData),
    url(r'^login', loginPage),
    url(r'^$', mainPage),
)
