from rest_framework.serializers import ModelSerializer

from inicio.models import Pelicula

class PeliculaListSerializer(ModelSerializer):
	class Meta:
		model = Pelicula
		fields = [
			'id',
			'nombre',
			'sinopsis'
		]	

class PeliculaRetrieveSerializer(ModelSerializer):
	class Meta:
		model = Pelicula
		fields = [
			'id',
			'sinopsis'
		]	
