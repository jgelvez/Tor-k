#! /usr/bin/python
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import login, logout, crear_cuenta

urlpatterns=patterns( '',  
  url(r'^login/$',  login, name='login'),
  url(r'^logout/$', logout, name='logout'),
  url(r'^crear_cuenta/$', crear_cuenta, name='crear_cuenta'),
)
 

