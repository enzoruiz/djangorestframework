from django.conf.urls import url
from .api.views import PeliculaListAPIView

urlpatterns = [
    url(r'^api-pelicula$', PeliculaListAPIView.as_view(), name="api-pelicula"),
]
