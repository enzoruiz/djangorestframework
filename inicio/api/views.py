from rest_framework.generics import (
	ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
)
from .serializers import (
	PeliculaListSerializer, PeliculaRetrieveSerializer,
	ActorPeliculaListSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import (
	SearchFilter, OrderingFilter
)
from .permissions import IsOwnerOrReadOnly
from .pagination import (
	PeliculaLimitOffsetPagination, PeliculaPageNumberPagination
)
from inicio.models import Pelicula, ActorPelicula


class PeliculaCreateAPIView(CreateAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = PeliculaRetrieveSerializer


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


class ActorPeliculaListAPIView(ListAPIView):
	queryset = ActorPelicula.objects.all()
	serializer_class = ActorPeliculaListSerializer
	permission_classes = [IsAuthenticated, ]
