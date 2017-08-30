from django.contrib.auth.models import User
from rest_framework.generics import (
	ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
)
from .serializers import (
	PeliculaListSerializer, PeliculaRetrieveSerializer,
	ActorListSerializer, ActorRetrieveSerializer, UserRetrieveSerializer,
	UserLoginSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.filters import (
	SearchFilter, OrderingFilter
)
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .permissions import IsOwnerOrReadOnly
from .pagination import (
	PeliculaLimitOffsetPagination, PeliculaPageNumberPagination,
	ActorPageNumberPagination
)
from inicio.models import Pelicula, Actor


class PeliculaCreateAPIView(CreateAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = PeliculaRetrieveSerializer

	# AGREGAR ALGO MAS ANTES DE CREAR
	def perfom_create(self, serializer):
		serializer.save(actor=self.request.user)


class PeliculaDetailAPIView(RetrieveAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = PeliculaRetrieveSerializer


class PeliculaUpdateAPIView(UpdateAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = PeliculaRetrieveSerializer


class PeliculaDeleteAPIView(DestroyAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = PeliculaRetrieveSerializer


class PeliculaListAPIView(ListAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = PeliculaListSerializer
	# permission_classes = [IsAuthenticated, ]

	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['nombre', 'director']
	pagination_class = PeliculaPageNumberPagination


class ActorListAPIView(ListAPIView):
	queryset = Actor.objects.all()
	serializer_class = ActorListSerializer
	# permission_classes = [IsAuthenticated, ]
	pagination_class = ActorPageNumberPagination


class ActorDetailAPIView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
	queryset = Actor.objects.all()
	serializer_class = ActorRetrieveSerializer
	# permission_classes = [IsAuthenticated, ]

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class UserCreateAPIView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserRetrieveSerializer


class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
