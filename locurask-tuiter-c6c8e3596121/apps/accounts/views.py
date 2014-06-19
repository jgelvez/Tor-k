#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.conf import settings
from django import forms
from apps.accounts.forms import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.views.decorators.cache import cache_control

    
@cache_control(must_revalidate=True, max_age=3600, private=True)
def login(request):
    
    
    base_url = "/"
    admin_url = "/admin/"
    
    if request.user.is_authenticated():
        return HttpResponseRedirect(base_url)
    
    if  request.method == 'POST':
        next =  request.POST.get('next', None)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password  =  form.data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Password valido, el usuario esta marcado como activo
                auth.login(request, user)
                # OK esta registrado lo redirecciono al home
                return HttpResponseRedirect(next)
        else:
            #le decimos que tiene errores
            return render_to_response("accounts/login.html", {'form':form, 'error':True, 'next':next}, context_instance = RequestContext(request))
    
    
    next =  request.GET.get('next', base_url)
    form = LoginForm()
    users = User.objects.all().order_by('username')
    values = {
           'form':form, 
           'next': next,
           'users':users,
    }
    return render_to_response("accounts/login.html", values, context_instance = RequestContext(request) )
    


@cache_control(must_revalidate=True, max_age=3600, private=True)
def logout(request):
    auth.logout(request)
    next =  request.GET.get('next', None)
    if next:
        url = next
    else:
        url = "/"
    return HttpResponseRedirect(url)


def crear_cuenta(request):

    if request.method == "POST":
        
        form = RegistracionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect( reverse('login') )
    
    else:
        form = RegistracionForm()

    values = {
        'title':'Crear una cuenta de usuario',
        'form':form,
    }

    return render_to_response("accounts/crear_cuenta.html", values, context_instance = RequestContext(request) )    
 
    
    
