from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ceph_dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ceph.views.base_view'),
    url(r'^demo', 'ceph.views.demo_view'),
)
