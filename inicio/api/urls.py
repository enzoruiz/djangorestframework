from django.conf.urls import url
from .views import (
    PeliculaListAPIView, PeliculaDetailAPIView, PeliculaUpdateAPIView,
    PeliculaDeleteAPIView, PeliculaCreateAPIView, ActorPeliculaListAPIView
)

urlpatterns = [
    url(r'^$', PeliculaListAPIView.as_view(), name="list-pelicula"),
    url(r'^(?P<pk>\d+)$',
        PeliculaDetailAPIView.as_view(), name="detail"),
    url(r'^create$',
        PeliculaCreateAPIView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/edit$',
        PeliculaUpdateAPIView.as_view(), name="update"),
    url(r'^(?P<pk>\d+)/delete$',
        PeliculaDeleteAPIView.as_view(), name="delete"),

    # url(r'^actor-pelicula$',
    #     ActorPeliculaListAPIView.as_view(), name="actor-pelicula"),
]
