from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from pets.reports import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^report-pets-by-tags/', login_required(views.report_pets_by_tags)),
)
