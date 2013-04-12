from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from pelis.models import *

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
				'titlehead': 'Movies',
				'pagetitle': 'Movies',
				'user': request.user,
				})
	output = template.render(variables)
	return HttpResponse(output)

def generepage(request):
	template = get_template('generepage.html')
	variables = Context({
				'titlehead': 'Genres',
				'pagetitle': 'Genres',
				'generes': Genere.objects.all()
				})
	output = template.render(variables)
	return HttpResponse(output)

def genereinfo(request, NomGenere):
	try:
		name = Genere.objects.get(NomGenere = NomGenere)
		titol = Pelicula.objects.filter(Genere = name)
	except Genere.DoesNotExist:
		raise Http404
	return render_to_response(
			'genereinfo.html',
			{
				'namegenere': name,
				'pelicules': titol
			})

def peliculespage(request):
	template = get_template('peliculespage.html')
	variables = Context({
				'titlehead': 'Movies',
				'pagetitle': 'Movies',
				'pelicules' : Pelicula.objects.all()
			})
	output = template.render(variables)
	return HttpResponse(output)

def peliculesinfo(request, idn):
	try:
		pelid = Pelicula.objects.get(id = idn)
	except Pelicula.DoesNotExist:
		raise Http404
	return render_to_response(
			'peliculesinfo.html',
			{
				'namepelicula': pelid,
				'pelicula': pelid,
				'actors': pelid.Actor.all()
			})

def actorspage(request):
	template = get_template('actorspage.html')
	variables = Context({
				'titlehead': 'Actors',
				'pagetitle': 'Actors',
				'actors' : Actor.objects.all()
			})
	output = template.render(variables)
	return HttpResponse(output)

def actorsinfo(request, idn):
	try:
		actorid = Actor.objects.get(id = idn)
		llistapeli=[]
		for peli in Pelicula.objects.all():
			for actor in peli.Actor.all():
				if (actor.id==actorid.id and peli not in llistapeli ):
					llistapeli.append(peli)
	except Actor.DoesNotExist:
		raise Http404
	return render_to_response(
			'actorsinfo.html',
			{
				'nameactor': actorid,
				'llistapelis': llistapeli

			})

def directorspage(request):
	template = get_template('directorspage.html')
	variables = Context({
				'titlehead': 'Directors',
				'pagetitle': 'Directors',
				'directors' : Director.objects.all()
			})
	output = template.render(variables)
	return HttpResponse(output)

def directorsinfo(request, idn):
	try:
		name = Director.objects.get(id = idn)
		titol = Pelicula.objects.filter(Director = name)
	except Director.DoesNotExist:
		raise Http404
	return render_to_response(
			'directorsinfo.html',
			{
				'namedirector': name,
				'pelis': titol
				
			})


