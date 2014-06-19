#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.PasswordInput()


attrs_dict = { 'class': 'required' }

class RegistracionForm(forms.Form):
    
    username = forms.RegexField(regex=r'^\w+$', max_length=30, widget=forms.TextInput(attrs=attrs_dict), label=_(u'Username'), required = True)
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=75)), label=_(u'Dirección de email'))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=_(u'Clave'))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=_(u'Clave (de nuevo)'))
    
    def clean_username(self):
        
        """
        Valida si el username ya existe en la base de datos
        """
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_(u'El nombre de usuario ya existe, por favor proporciona otro nombre de usuario'))
    
    
    def clean(self):
        """
        Verificamos si password1 y password2 son iguales
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_(u'Tienes que ingresar la misma clave en los dos campos'))
        return self.cleaned_data
    
        
    def save(self, profile_callback=None):
        """
        Creamos el usuario, el cliente y relacionamos el cliente con el usuario
        """
        
        username = self.cleaned_data['username']
        password = self.cleaned_data['password1']
        email    = self.cleaned_data['email']
        
        usuario = User.objects.create_user(username, email, password)
        usuario.is_active = True
        usuario.save()
        
        return usuario