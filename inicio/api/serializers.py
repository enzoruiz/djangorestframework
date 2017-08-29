from rest_framework.serializers import (
	ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
)
from inicio.models import Pelicula, ActorPelicula


class ActorPeliculaListSerializer(ModelSerializer):
	nombre_actor = SerializerMethodField()

	class Meta:
		model = ActorPelicula
		fields = [
			'id',
			'nombre_actor',
			'nombre_personaje',
		]

	def get_nombre_actor(self, obj):
		return str(obj.actor)


class PeliculaListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='detail',
		lookup_field='pk'
	)

	class Meta:
		model = Pelicula
		fields = [
			'url',
			'id',
			'nombre',
			'sinopsis'
		]


class PeliculaRetrieveSerializer(ModelSerializer):
	actores = SerializerMethodField()

	class Meta:
		model = Pelicula
		fields = [
			'id',
			'nombre',
			'sinopsis',
			'director',
			'fecha_estreno',
			'actores'
		]

	def get_actores(self, obj):
		actores = ActorPelicula.objects.filter(pelicula=obj)
		if actores.count() > 0:
			lista = ActorPeliculaListSerializer(actores, many=True).data
		else:
			lista = None
		return lista
