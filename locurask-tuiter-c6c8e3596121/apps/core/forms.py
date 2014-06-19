#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms 
from apps.core.models import Tuit, UserProfile
    
class TuitForm(forms.ModelForm):
	"""
	Este es el formulario para que podamos tuitear
	""" 
	class Meta:
		model = Tuit 
		exclude = ('usuario', 'fecha_de_publicacion')



class UserProfileForm(forms.ModelForm):
	"""
	Este es el formulario para editar el profile de cada usuario
	"""
	class Meta:
		model = UserProfile
		exclude = ('user', 'siguiendo_a')


