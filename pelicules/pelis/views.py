from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from pelis import *
import pelis.models

def mainpage(request):
	return render_to_response(
			'mainpage.html',
			{
				'titlehead': 'Pelicules',
				'pagetitle': 'Benvingut a Pelicules',
				'user': request.user,
			})

def generepage(request):
	return render_to_response(
			'generepage.html',
			{
				'titlehead': 'Genere',
				'pagetitle': 'Genere',
				'list' : models.Genere.objects.all(),
			})

def peliculespage(request):
	return render_to_response(
			'peliculespage.html',
			{
				'titlehead': 'Pelicules',
				'pagetitle': 'Pelicules',
				'list' : models.Pelicula.objects.all(),
			})

def actorspage(request):
	return render_to_response(
			'actorspage.html',
			{
				'titlehead': 'Actors',
				'pagetitle': 'Actors',
				'list' : models.Actor.objects.all(),
			})

def directorspage(request):
	return render_to_response(
			'directorspage.html',
			{
				'titlehead': 'Directors',
				'pagetitle': 'Directors',
				'list' : models.Director.objects.all(),
			})

def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')

	pelicules = user.pelicula_set.all()
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		'pelicules': pelicules
		})
	output = template.render(variables)
	return HttpResponse(output)


