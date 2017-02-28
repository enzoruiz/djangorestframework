from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .serializers import PeliculaListSerializer, PeliculaRetrieveSerializer, ActorPeliculaListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from inicio.models import Pelicula, ActorPelicula

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
	permission_classes = [IsAuthenticated, ]

class ActorPeliculaListAPIView(ListAPIView):
	queryset = ActorPelicula.objects.all()
	serializer_class = ActorPeliculaListSerializer
	permission_classes = [IsAuthenticated, ]