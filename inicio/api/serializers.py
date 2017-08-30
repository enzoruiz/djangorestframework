from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.serializers import (
	EmailField, CharField,
	ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
)
from rest_framework.exceptions import ValidationError
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


class UserRetrieveSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email'
		]
		extra_kwargs = {
			'password': {
				'write_only': True
			}
		}

	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		user = User(
			username=username,
			email=email
		)
		user.set_password(password)
		user.save()

		return validated_data


class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField(required=False, allow_blank=True)
	email = EmailField(required=False, allow_blank=True)

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'token'
		]
		extra_kwargs = {
			'password': {
				'write_only': True
			}
		}

	def validate(self, data):
		user_obj = None
		username = data.get('username', None)
		email = data.get('email', None)
		password = data['password']

		if not username and not email:
			raise ValidationError('Username o Email es obligatorio para Login')

		user = User.objects.filter(
			Q(email=email) |
			Q(username=username)
		).distinct()

		if user.exists() and user.count() == 1:
			user_obj = user.first()
		else:
			raise ValidationError('El usuario o email no es valido.')

		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError('Credenciales invalidas, intentelo de nuevo.')

		data['token'] = 'ALGUN TOKEN'

		return data

	# def create(self, validated_data):
	# 	username = validated_data['username']
	# 	email = validated_data['email']
	# 	password = validated_data['password']
	# 	user = User(
	# 		username=username,
	# 		email=email
	# 	)
	# 	user.set_password(password)
	# 	user.save()
	#
	# 	return validated_data
