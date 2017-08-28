from rest_framework.serializers import ModelSerializer, SerializerMethodField

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
	actores = SerializerMethodField()

	class Meta:
		model = Pelicula
		fields = [
			'id',
			'nombre',
			'sinopsis',
			'actores'
		]

	def get_actores(self, obj):
		actores = ActorPelicula.objects.filter(pelicula=obj)
		if actores.count() > 0:
			lista = ActorPeliculaListSerializer(actores, many=True).data
		else:
			lista = None
		return lista


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
