#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.core.views.home', name='home'),
    url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^core/', include('apps.core.urls')),    
    url(r'^(?P<nombre>\w+)/$', 'apps.core.views.usuario_seleccionado', name='usuario_seleccionado'),
    url(r'^pdf/', include('apps.pdf.urls')),
)
