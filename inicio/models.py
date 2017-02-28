from django.db import models

# Create your models here.

class Pelicula(models.Model):
	nombre = models.CharField(max_length=140)
	sinopsis = models.TextField()
	director = models.CharField(max_length=140)
	fecha_estreno = models.DateField()

	def __str__(self):
		return self.nombre