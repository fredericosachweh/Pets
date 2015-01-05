from django.conf.urls import patterns, include, url
from django.contrib import admin
from pets.reports import urls as reports_url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/reports/', include(reports_url)),
    url(r'^admin/', include(admin.site.urls)),
)
