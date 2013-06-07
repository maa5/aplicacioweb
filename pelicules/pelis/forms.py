from django.forms import ModelForm
from models import Pelicula, Director, Actor, Genere, Review

class PeliculaForm(ModelForm):
	class Meta:
		model = Pelicula
		exclude = ('user')

class GenereForm(ModelForm):
	class Meta:
		model = Genere
		exclude = ('user')

class DirectorForm(ModelForm):
	class Meta: 
		model = Director
		exclude = ('user')

class ActorForm(ModelForm):
	class Meta: 
		model = Actor
		exclude = ('user')

