from django.conf.urls import url
from .api.views import PeliculaListAPIView, PeliculaDetailAPIView, PeliculaUpdateAPIView, PeliculaDeleteAPIView, ActorPeliculaListAPIView

urlpatterns = [
    url(r'^api-pelicula$', PeliculaListAPIView.as_view(), name="api-pelicula"),
    url(r'^api-pelicula/(?P<pk>[\w-]+)/$', PeliculaDetailAPIView.as_view(), name="detail"),
    url(r'^api-pelicula/(?P<pk>[\w-]+)/edit/$', PeliculaUpdateAPIView.as_view(), name="update"),
    url(r'^api-pelicula/(?P<pk>[\w-]+)/delete/$', PeliculaDeleteAPIView.as_view(), name="delete"),
    
    url(r'^actor-pelicula$', ActorPeliculaListAPIView.as_view(), name="actor-pelicula"),
]
