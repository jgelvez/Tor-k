#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals


from datetime import datetime


class UserProfile(models.Model):
	"""
		El profile de cada usuario
	"""

	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to='avatars/%d/%m/%Y', null=True, blank=True)
	descripcion = models.TextField("Descripción o firma")
	website = models.URLField(null=True, blank=True)
	siguiendo_a = models.ManyToManyField('self', related_name='seguido_por', symmetrical=False)
	
	def __unicode__(self):
		return u"%s" % self.user  

	def seguir_a(self, user):
		self.siguiendo_a.add( user.get_profile() )
		return

	def dejar_de_seguir_a(self, user):
		self.siguiendo_a.remove( user.get_profile() )
		return 

	def obtener_tuits_seguidos(self):
		return Tuit.objects.filter(usuario__in=self.siguiendo_a.all())

	def obtener_tuits_seguidos_y_los_mios(self):
		users = [ p for p in self.siguiendo_a.all() ]
		users.append( self )
		tuits = Tuit.objects.filter(usuario__in = users )
		return tuits

	def estamos_siguiendo_al_usuario(self, user):
		return self.siguiendo_a.filter(id=user.get_profile().id).exists()
	
	def cantidad_de_tuits_creados(self):
		return Tuit.objects.filter(usuario = self.user).count()



class Tuit(models.Model):
	"""
		La representacion de un tuit 
	"""
	texto = models.CharField("Que estas pensando ?", max_length=240)
	usuario = models.ForeignKey(User)
	fecha_de_publicacion = models.DateTimeField(null=False, blank=False, default = datetime.now() )

	def __unicode__(self):
		return u"%s..." % self.texto[:20]

	def puedo_eliminar(self, user):
		"""este metodo se encarga de verificar si se puede eliminar el tuit"""
		return self.usuario == user

	class Meta():
		ordering = ['-id']

	




#========================================================
# Signals
#========================================================
def crear_user_profile(sender, instance, created, **kwargs):  
	"""
		Cuando se crea un usuario en la base de datos vamos a crear su profile 
		hookeandonos al evento emitido por el objeto User al momento 
		de hacer un post_save 
	"""
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)

signals.post_save.connect(crear_user_profile, sender=User) 





class Persona(models.Model):
	nombre = models.CharField(max_length=240)

	def __unicode__(self):
		return self.nombre


class Libro(models.Model):
	titulo = models.CharField(max_length=240)
	autor = models.ForeignKey(Persona, related_name="creado_por")
	editor = models.ForeignKey(Persona, related_name="editado_por")

	def __unicode__(self):
		return self.titulo

