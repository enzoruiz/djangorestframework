from rest_framework.generics import ListAPIView
from .serializers import PeliculaSerializer
from inicio.models import Pelicula

class PeliculaListAPIView(ListAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = PeliculaSerializer
