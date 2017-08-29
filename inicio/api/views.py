from rest_framework.generics import (
	ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
)
from .serializers import (
	PeliculaListSerializer, PeliculaRetrieveSerializer,
	ActorListSerializer, ActorRetrieveSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import (
	SearchFilter, OrderingFilter
)
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

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
