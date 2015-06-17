# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^myapp/', include('myproject.myapp.urls')),
	(r'^$', RedirectView.as_view(url='/myapp/documents/')), # Just for ease of use.
	#(r'^$', 'myapp.views.documents'), # Just for ease of use.
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/',     include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
