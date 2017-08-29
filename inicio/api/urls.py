from django.conf.urls import url
from .views import (
    PeliculaListAPIView, PeliculaDetailAPIView, PeliculaUpdateAPIView,
    PeliculaDeleteAPIView, PeliculaCreateAPIView, ActorListAPIView, ActorDetailAPIView
)

urlpatterns = [
    url(r'^peliculas/$', PeliculaListAPIView.as_view(), name="list-pelicula"),
    url(r'^peliculas/(?P<pk>\d+)$',
        PeliculaDetailAPIView.as_view(), name="detail-pelicula"),
    url(r'^peliculas/create$',
        PeliculaCreateAPIView.as_view(), name="create-pelicula"),
    url(r'^peliculas/(?P<pk>\d+)/edit$',
        PeliculaUpdateAPIView.as_view(), name="update-pelicula"),
    url(r'^peliculas/(?P<pk>\d+)/delete$',
        PeliculaDeleteAPIView.as_view(), name="delete-pelicula"),

    url(r'^actores/$',
        ActorListAPIView.as_view(), name="list-actor"),
    url(r'^actores/(?P<pk>\d+)$',
        ActorDetailAPIView.as_view(), name="detail-actor"),
]
