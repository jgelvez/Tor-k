#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import *

class TuitAdmin(admin.ModelAdmin):
	list_display = 'texto', 'usuario'
	list_filter = ('usuario', )
admin.site.register(Tuit, TuitAdmin)
