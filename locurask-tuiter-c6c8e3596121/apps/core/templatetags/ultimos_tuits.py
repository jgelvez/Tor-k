#! /usr/bin/python
# -*- encoding: utf-8 -*-
from django import template
from django.template import Context
from apps.core.models import *

register = template.Library()


@register.inclusion_tag('templatetags/mostrar_ultimos_tuits.html', takes_context = True)
def mostrar_ultimos_tuits(context, periodo=None):
	
	tuits = Tuit.objects.all()[:10]
	total = tuits.count()
	values = {
		'tuits':tuits,
		'total':total,
	}

	return values


