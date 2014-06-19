#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.conf import settings

from apps.core.models import *
from apps.core.forms import TuitForm, UserProfileForm
import simplejson


def home(request):

	if not request.user.is_authenticated():	
		values = {
			'title':'Bienvenido a tuiter'
		}
		return render_to_response("core/bienvenido.html", values, context_instance=RequestContext(request))


	if request.method == "POST":
		form = TuitForm(request.POST)
		if form.is_valid():

			tuit = form.save(commit=False)
			tuit.usuario = request.user
			tuit.save()
			form = TuitForm()

	else:
		form = TuitForm()

	
	ultimos_tuits = request.user.get_profile().obtener_tuits_seguidos_y_los_mios()

	values = {
		'title':'Hola %s ' % request.user,
		'ultimos_tuits':ultimos_tuits,
		'form':form,
		
	}

	return render_to_response("core/micuenta.html", values, context_instance=RequestContext(request))	



def usuario_seleccionado(request, nombre ):
	
	usuario = get_object_or_404(User, username = nombre )

	es_tu_usuario = False
	lo_seguis = False
	te_sigue = False

	if request.user.is_authenticated():
		if request.user == usuario:
			es_tu_usuario = True
		else:
			lo_seguis = request.user.get_profile().estamos_siguiendo_al_usuario(usuario)
			te_sigue = usuario.get_profile().estamos_siguiendo_al_usuario(request.user)


	ultimos_tuits = Tuit.objects.filter(usuario = usuario)

	values = {
		'title':'Tuits de %s ' % usuario,
		'usuario':usuario,
		'ultimos_tuits':ultimos_tuits,
		'es_tu_usuario': es_tu_usuario,
		'lo_seguis': lo_seguis,
		'te_sigue': te_sigue,
	}	

	return render_to_response("core/usuario_seleccionado.html", values, context_instance=RequestContext(request))	
   



@csrf_exempt
@login_required
def eliminar_tuit(request, id_tuit):

	tuit = get_object_or_404(Tuit, id = id_tuit) 
	data = {'success':False, 'msg':'No se pudo eliminar el tuit' }

	if tuit.puedo_eliminar(request.user):
		tuit.delete()
		cant_tuits = request.user.get_profile().cantidad_de_tuits_creados()
	 	data = {
	 		'success':True, 
	 		'msg':'Se elimino el tuit',
	 		'cant_tuits': cant_tuits }

 	json = simplejson.dumps(data, ensure_ascii=False, indent=4)
 	return HttpResponse(json, mimetype = 'application/json')


@login_required
def editar_perfil(request):
	
	profile = request.user.get_profile()

	if request.method == "POST":
		form = UserProfileForm(request.POST, request.FILES, instance = profile)
		if form.is_valid():
			form.save()

			#mas info sobre reverse:
			#https://docs.djangoproject.com/en/dev/topics/http/urls/
			return HttpResponseRedirect( reverse('home') )
		
	else:
		form = UserProfileForm( instance = profile )

	values = {
		'title':'Editando tu perfil',
		'form':form,
	}
	return render_to_response("core/editar_perfil.html", values, context_instance=RequestContext(request))	


@login_required
def seguir_a(request, id_usuario):

	usuario = get_object_or_404(User, id = id_usuario)

	mi_profile = request.user.get_profile()

	mi_profile.seguir_a(usuario)

	return HttpResponseRedirect( reverse('usuario_seleccionado', args=(usuario.username,)  ) )




@login_required
def dejar_de_seguir_a(request, id_usuario):

	usuario = get_object_or_404(User, id = id_usuario)

	mi_profile = request.user.get_profile()

	mi_profile.dejar_de_seguir_a(usuario)

	return HttpResponseRedirect( reverse('usuario_seleccionado', args=(usuario.username,)  ) )






