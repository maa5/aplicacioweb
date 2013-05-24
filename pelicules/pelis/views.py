from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from pelis.models import *
from forms import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from serializers import PeliculesSerializer, GeneresSerializer, ActorsSerializer, DirectorsSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

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
				'pelicules' : Pelicula.objects.all(),
				'user': request.user
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
				'actors' : Actor.objects.all(),
				'user': request.user
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
				'directors' : Director.objects.all(),
				'user': request.user
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

def userpage(request, username):

	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	return render_to_response(
			'userpage.html',
			{
				'username':username,
			})

# Detail
class PeliculaDetail(DetailView):
	model = Pelicula
	template_name = 'peliculespage.html'

	def get_context_data(self, **kwargs):
		context = super(PeliculaDetail, self).get_context_data(**kwargs)
		return context

class GenereDetail(DetailView):
	model = Pelicula
	template_name = 'generepage.html'

	def get_context_data(self, **kwargs):
		context = super(PeliculaDetail, self).get_context_data(**kwargs)
		return context

class ActorDetail(DetailView):
	model = Pelicula
	template_name = 'actorspage.html'

	def get_context_data(self, **kwargs):
		context = super(GenereDetail, self).get_context_data(**kwargs)
		return context

class DirectorDetail(DetailView):
	model = Pelicula
	template_name = 'directorspage.html'

	def get_context_data(self, **kwargs):
		context = super(DirectorDetail, self).get_context_data(**kwargs)
		return context

# Create
class PeliculaCreate(CreateView):
	model = Pelicula
	template_name = 'formcreate.html'
	form_class = PeliculaForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(PeliculaCreate, self).form_valid(form)

class ActorCreate(CreateView):
	model = Actor
	template_name = 'formcreate.html'
	form_class = ActorForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ActorCreate, self).form_valid(form)

class DirectorCreate(CreateView):
	model = Director
	template_name = 'formcreate.html'
	form_class = DirectorForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(DirectorCreate, self).form_valid(form)

# Delete
class PeliculaDelete(DeleteView):
	model = Pelicula
	template_name = 'delete.html'
	success_url = '/pelicules'

class ActorDelete(DeleteView):
	model = Actor
	template_name = 'delete.html'
	success_url = '/actors'

class DirectorDelete(DeleteView):
	model = Director
	template_name = 'delete.html'
	success_url = '/directors'

# RESTful API
class APIPeliculesList(generics.ListCreateAPIView):
	model = Pelicula
	serializer_class = PeliculesSerializer

class APIPeliculesDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Pelicula
	serializer_class = PeliculesSerializer

class APIGeneresList(generics.ListCreateAPIView):
	model = Genere
	serializer_class = GeneresSerializer

class APIGeneresDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Genere
	serializer_class = GeneresSerializer

class APIActorsList(generics.ListCreateAPIView):
	model = Actor
	serializer_class = ActorsSerializer

class APIActorsDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Actor
	serializer_class = ActorsSerializer

class APIDirectorsList(generics.ListCreateAPIView):
	model = Director
	serializer_class = DirectorsSerializer

class APIDirectorsDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Director
	serializer_class = DirectorsSerializer





