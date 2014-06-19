#! /usr/bin/python
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import testpdf

urlpatterns=patterns( '',  
  url(r'^test/$',  testpdf, name='testpdf'),
)
 