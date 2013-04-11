from django.db import models

# Create your models here.

class Director(models.Model):
	Nom = models.TextField(max_length=50)
	Cognom = models.TextField(max_length=50)
	def __str__(self):
			return '%s %s' % (self.Nom, self.Cognom)

class Genere(models.Model):
	NomGenere = models.TextField(max_length=50)
	def __str__(self):
			return self.NomGenere

class Actor(models.Model):
	Nom = models.TextField(max_length=50, blank=True)
	Cognom = models.TextField(max_length=50, blank=True)
	def __str__(self):
			return '%s %s' % (self.Nom, self.Cognom)

class Pelicula(models.Model):
	Titol = models.TextField(max_length=50)
	Data = models.IntegerField()
	Argument = models.TextField(max_length=300)
	Director = models.ForeignKey(Director)
	Genere = models.ForeignKey(Genere)
	Actor = models.ManyToManyField(Actor)
	def __str__(self):
			return self.Titol




