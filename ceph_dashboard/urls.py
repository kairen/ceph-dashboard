from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ceph_dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'ceph.views.cluster_health_view'),
    url(r'^health', 'ceph.views.cluster_health_view'),
    url(r'^osd', 'ceph.views.cluster_osd_view'),
    url(r'^mon', 'ceph.views.cluster_mon_view'),
)
