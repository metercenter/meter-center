from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#url(r'^init/', include('testapp.urls', namespace="testapp")),
    url(r'^datacenter/', include('datahandle.urls', namespace="datahandle")),
    url(r'^login/', include('online.urls', namespace="online")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/home/shu/test/python/mysite/'}),  
)
