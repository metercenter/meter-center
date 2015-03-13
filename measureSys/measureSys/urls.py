from django.conf.urls import patterns, include, url
from django.contrib import admin
from meter.views import mainPage, logout_view
from meter.views import getMeter
from meter.views import userList
from meter.views import getData
from meter.views import loginPage
from meter.views import login_view, user_group_show,user_level,register_company,register_meter,meter_level

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Measuringsystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get-meter', getMeter),
    url(r'^Users/List', userList),
    url(r'^get-data', getData),
    url(r'^$', loginPage),
    url(r'^login', loginPage),
    url(r'^Logout',logout_view),
    url(r'^main',login_view),
    url(r'^get-user-group',user_group_show),
    url(r'^get-user-level',user_level),
    url(r'^get-usermeter-level',meter_level),
    url(r'^register_company',register_company),
    url(r'^register_meter',register_meter),
)
