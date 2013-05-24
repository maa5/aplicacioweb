from django.conf.urls import patterns, include, url
from pelis.views import *
from django.views.generic import DetailView, UpdateView, DeleteView
from pelis.models import *
from pelis.forms import PeliculaForm, GenereForm, ActorForm, DirectorForm
from pelis.views import PeliculaCreate, ActorCreate, DirectorCreate
from django.utils import timezone
from pelis.views import APIPeliculesList, APIPeliculesDetail, APIGeneresList, APIGeneresDetail, \
			     APIActorsList, APIActorsDetail, APIDirectorsList, APIDirectorsDetail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pelicules.views.home', name='home'),
	 url(r'^$', mainpage, name='home'),
	 url(r'^login/$','django.contrib.auth.views.login'),
	 url(r'^logout/$', 'django.contrib.auth.views.logout'),
	 url(r'^user/(\w+)/$', userpage),
    #url(r'^pelicules/', include('pelicules.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   	 url(r'^admin/', include(admin.site.urls)),

	 # Create
	 url(r'^pelicules/create/$', 
		PeliculaCreate.as_view(),
		name = 'pelicula_create'),
	 url(r'^actors/create/$', 
		ActorCreate.as_view(),
		name = 'actor_create'),
	 url(r'^directors/create/$', 
		DirectorCreate.as_view(),
		name = 'director_create'),

	 # Edit
	 url(r'^pelicules/(?P<pk>\d+)/edit/$',
	 	UpdateView.as_view(model = Pelicula, 
	 	template_name = 'formedit.html',
	 	form_class = PeliculaForm),
	 	name='pelicula_edit'),
    url(r'^actors/(?P<pk>\d+)/edit/$',
	 	UpdateView.as_view(model = Actor, 
	 	template_name = 'formedit.html',
	 	form_class = ActorForm),
	 	name='actor_edit'),
    url(r'^directors/(?P<pk>\d+)/edit/$',
	 	UpdateView.as_view(model = Director, 
	 	template_name = 'formedit.html',
	 	form_class = DirectorForm), 
	 	name='director_edit'),

	 # List
	 url(r'^generes/$', generepage),
	 url(r'^pelicules/$', peliculespage),
	 url(r'^actors/$', actorspage),
	 url(r'^directors/$', directorspage),

	 # Detail	
    url(r'^pelicules/(?P<idn>\d+)/$', peliculesinfo, name='pelicula_detail'),
    url(r'^generes/(?P<NomGenere>\w+)/$', genereinfo, name='genere_detail'),
    url(r'^actors/(?P<idn>\d+)/$', actorsinfo, name='actor_detail'),
    url(r'^directors/(?P<idn>\d+)/$', directorsinfo, name='director_detail'),
	 	
	 # Delete
	 url(r'^pelicules/(?P<pk>\d+)/delete/$',
		PeliculaDelete.as_view(),
		name='pelicula_delete'),
    url(r'^actors/(?P<pk>\d+)/delete/$',
		ActorDelete.as_view(),
		name='actor_delete'),
    url(r'^directors/(?P<pk>\d+)/delete/$',
		DirectorDelete.as_view(),
		name='director_delete'),

	 # RESTful API
    url(r'^api/pelicules/$', APIPeliculesList.as_view(), name='pelicules-list'),
    url(r'^api/pelicules/(?P<pk>\d+)/$', APIPeliculesDetail.as_view(), name='pelicules-detail'),
    url(r'^api/generes/$', APIGeneresList.as_view(), name='generes-list'),
    url(r'^api/generes/(?P<pk>\d+)/$', APIGeneresList.as_view(), name='generes-detail'),
    url(r'^api/actors/$', APIActorsList.as_view(), name='actors-list'),
    url(r'^api/actors/(?P<pk>\d+)/$', APIActorsDetail.as_view(), name='actors-detail'),
	 url(r'^api/directors/$', APIDirectorsList.as_view(), name='directors-list'),
    url(r'^api/directors/(?P<pk>\d+)/$', APIDirectorsDetail.as_view(), name='directors-detail'),
)
