from django.conf.urls import patterns, include, url
from django.contrib import admin
from meter.views import mainPage
from meter.views import getMeter
from meter.views import userList
from meter.views import getData
from meter.views import loginPage
from meter.views import login_view, user_group_show

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
    url(r'^main',login_view),
    url(r'^get-user-group',user_group_show),
)
