from django.conf.urls import patterns, include, url
from django.contrib import admin
from tork.views import hora_actual, hora_demas, pagina_inicio

admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),

    (r'^index/$', pagina_inicio),
	(r'^hora/$', hora_actual),
	(r'^hora/mas/(\d{1,2})/$', hora_demas),
)
