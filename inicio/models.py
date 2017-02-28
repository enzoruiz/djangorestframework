from django.db import models

# Create your models here.

class Pelicula(models.Model):
	nombre = models.CharField(max_length=140)
	sinopsis = models.TextField()
	director = models.CharField(max_length=140)
	fecha_estreno = models.DateField()

	def __str__(self):
		return self.nombre

class Actor(models.Model):
	nombres = models.CharField(max_length=140)
	apellidos = models.CharField(max_length=140)

	def __str__(self):
		return self.nombres + ' ' + self.apellidos

class ActorPelicula(models.Model):
	actor = models.ForeignKey(Actor)
	pelicula = models.ForeignKey(Pelicula)
	nombre_personaje = models.CharField(max_length=140)

	def __str__(self):
		return str(self.pelicula) + ' - ' + str(self.actor)