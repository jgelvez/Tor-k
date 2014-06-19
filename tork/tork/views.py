from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def hora_actual(request):
	now = datetime.datetime.now()
	t = get_template('hora_actual.html')
	html = t.render(Context({'hora': now}))
	return HttpResponse(html)

def hora_demas(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>En %s horas, seran las %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def pagina_inicio(request):
	return render_to_response('internet/base_navbar.html')
