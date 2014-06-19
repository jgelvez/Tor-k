#! /usr/bin/python
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *

urlpatterns=patterns( '',  
    url(r'^editar_perfil/$', editar_perfil, name='editar_perfil'),
    url(r'^eliminar_tuit/(?P<id_tuit>\d+)/$', eliminar_tuit, name='editar_perfil'),
    url(r'^seguir_a/(?P<id_usuario>\d+)/$', seguir_a , name='seguir_a'),
    url(r'^dejar_de_seguir_a/(?P<id_usuario>\d+)/$', dejar_de_seguir_a , name='dejar_de_seguir_a'),
)
 

