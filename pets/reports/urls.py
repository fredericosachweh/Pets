from django.conf.urls import patterns, url
from pets.reports import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^report-pets-by-tags/', views.report_pets_by_tags, name='report-pets-by-tags'),
)
