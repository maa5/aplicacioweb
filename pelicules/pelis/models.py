from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class Director(models.Model):
	Nom = models.TextField(max_length=50)
	Cognom = models.TextField(max_length=50)
	date = models.DateField()
	Descripcio=models.TextField(max_length=500)
	Foto=models.TextField(max_length=100)
	user = models.ForeignKey(User)

	def __str__(self):
			return '%s %s' % (self.Nom, self.Cognom)
	def get_absolute_url(self):
			return reverse('director_detail', kwargs={'idn': self.pk})

class Genere(models.Model):
	tipus=(
		('Accio','Accio'),('Aventura','Aventura'),('CienciaFiccio','CienciaFiccio'),
		('Comedia','Comedia'),('Drama','Drama'),('Terror','Terror'),('Thriller','Thriller'),
	)
	NomGenere = models.CharField(max_length=50,choices=tipus,unique=True)

	def __str__(self):
			return self.NomGenere
	def get_absolute_url(self):
			return reverse('genere_detail', kwargs={'idn': self.pk})

class Actor(models.Model):
	Nom = models.TextField(max_length=50, blank=True)
	Cognom = models.TextField(max_length=50, blank=True)
	date = models.DateField()
	descripcio=models.TextField(max_length=500)
	Foto=models.TextField(max_length=100)
	user = models.ForeignKey(User)

	def __str__(self):
			return '%s %s' % (self.Nom, self.Cognom)
	def get_absolute_url(self):
			return reverse('actor_detail', kwargs={'idn': self.pk})

class Pelicula(models.Model):
	Titol = models.TextField(max_length=50)
	Data = models.IntegerField()
	Argument = models.TextField(max_length=300)
	Director = models.ForeignKey(Director)
	Genere = models.ForeignKey(Genere)
	Foto=models.TextField(max_length=100)
	Actor = models.ManyToManyField(Actor)
	user = models.ForeignKey(User)

	def __str__(self):
			return self.Titol
	def get_absolute_url(self):
			return reverse('pelicula_detail', kwargs={'idn': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)

class PeliculesReview(Review):
    Pelicula = models.ForeignKey(Pelicula)




