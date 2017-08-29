from rest_framework.serializers import (
	ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
)
from inicio.models import Pelicula, ActorPelicula, Actor


class ActorListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='detail-actor',
		lookup_field='pk'
	)

	class Meta:
		model = Actor
		fields = [
			'url',
			'id',
			'nombres',
			'apellidos',
		]


class ActorRetrieveSerializer(ModelSerializer):
	peliculas = SerializerMethodField()

	class Meta:
		model = Actor
		fields = [
			'nombres',
			'apellidos',
			'peliculas'
		]

	def get_peliculas(self, obj):
		peliculas = ActorPelicula.objects.filter(actor=obj)
		if peliculas.count() > 0:
			return PeliculaActorListSerializer(peliculas, many=True).data
		else:
			return None


# DETALLE DE LISTA DE ACTORES EN UNA PELICULA
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
		return "%s %s" % (str(obj.actor.nombres), str(obj.actor.apellidos))


# DETALLE DE LISTA DE PELICULAS DE UN ACTOR
class PeliculaActorListSerializer(ModelSerializer):
	nombre = SerializerMethodField()
	sinopsis = SerializerMethodField()
	fecha_estreno = SerializerMethodField()

	class Meta:
		model = ActorPelicula
		fields = [
			'id',
			'nombre',
			'nombre_personaje',
			'sinopsis',
			'fecha_estreno',
		]

	def get_nombre(self, obj):
		return str(obj.pelicula.nombre)

	def get_sinopsis(self, obj):
		return str(obj.pelicula.sinopsis)

	def get_fecha_estreno(self, obj):
		return str(obj.pelicula.fecha_estreno)


class PeliculaListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name='detail-pelicula',
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

		read_only_fields = [
			'fecha_estreno',
			'director',
			'nombre'
		]

	def get_actores(self, obj):
		actores = ActorPelicula.objects.filter(pelicula=obj)
		if actores.count() > 0:
			lista = ActorPeliculaListSerializer(actores, many=True).data
		else:
			lista = None
		return lista
