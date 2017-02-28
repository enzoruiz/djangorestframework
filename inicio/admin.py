from django.contrib import admin
from .models import Pelicula, Actor, ActorPelicula

# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Actor)
admin.site.register(ActorPelicula)