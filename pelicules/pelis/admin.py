from django.contrib import admin
from pelis.models import Pelicula, Director, Genere, Actor, PeliculesReview

admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Genere)
admin.site.register(Actor)
admin.site.register(PeliculesReview)
