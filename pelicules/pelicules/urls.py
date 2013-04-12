from django.conf.urls import patterns, include, url
from pelis.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pelicules.views.home', name='home'),
	 url(r'^$', mainpage, name='home'),
	 url(r'^login/$','django.contrib.auth.views.login'),
	 url(r'^generes/$', generepage),
	 url(r'^generes/(?P<NomGenere>\w+)/$', genereinfo),
	 url(r'^pelicules/$', peliculespage),
	 url(r'^pelicules/(?P<idn>\d+)/$', peliculesinfo),
	 url(r'^actors/$', actorspage),
	 url(r'^actors/(?P<idn>\d+)/$', actorsinfo),
	 url(r'^directors/$', directorspage),
	 url(r'^directors/(?P<idn>\d+)/$', directorsinfo),
    #url(r'^pelicules/', include('pelicules.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
