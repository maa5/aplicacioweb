from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class PeliculesSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='pelicules-detail')
	Director = HyperlinkedRelatedField(many=False, read_only=True, view_name='directors-detail')
	Genere = HyperlinkedRelatedField(many=False, read_only=True, view_name='generes-detail')
	Actor = HyperlinkedRelatedField(many=True, read_only=True, view_name='actors-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Pelicula
		fields = ('url', 'Titol', 'Data', 'Argument', 'Director', 'Genere', 'Foto', 'Actor', 'user')

class GeneresSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='generes-detail')
	pelicula_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='pelicules-detail')

	class Meta:
		model = Genere
		fields = ('url', 'NomGenere', 'pelicula_set')

class ActorsSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='actors-detail')
	pelicula_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='pelicules-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Actor
		fields = ('url', 'Nom', 'Cognom', 'date', 'descripcio', 'Foto', 'user', 'pelicula_set')

class DirectorsSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='directors-detail')
	pelicula_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='pelicules-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Director
		fields = ('url', 'Nom', 'Cognom', 'date', 'Descripcio', 'Foto', 'user', 'pelicula_set')

