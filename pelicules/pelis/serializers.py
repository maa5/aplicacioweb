from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class PeliculesSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='pelicula-detail')
	Director = HyperlinkedRelatedField(many=False, read_only=True, view_name='director-detail')
	Genere = HyperlinkedRelatedField(many=False, read_only=True, view_name='genere-detail')
	Actor = HyperlinkedRelatedField(many=True, read_only=True, view_name='actor-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Pelicula
		fields = ('url', 'Titol', 'Data', 'Argument', 'Director', 'Genere', 'Foto', 'Actor', 'user')

class GeneresSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='genere-detail')
	pelicula_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='pelicula-detail')

	class Meta:
		model = Genere
		fields = ('url', 'NomGenere', 'pelicula_set')

class ActorsSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='actor-detail')
	pelicula_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='pelicula-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Actor
		fields = ('url', 'Nom', 'Cognom', 'date', 'descripcio', 'Foto', 'user', 'pelicula_set')

class DirectorsSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='director-detail')
	pelicula_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='pelicula-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Director
		fields = ('url', 'Nom', 'Cognom', 'date', 'Descripcio', 'Foto', 'user', 'pelicula_set')

