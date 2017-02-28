from rest_framework.serializers import ModelSerializer

from inicio.models import Pelicula

class PeliculaSerializer(ModelSerializer):
	class Meta:
		model = Pelicula
		fields = [
			'id',
			'nombre',
			'sinopsis'
		]
