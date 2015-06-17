# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^documents/$', 'documentsView', name='documents'),
    url(r'^patientsEval/$', 'patientsEvalView', name='patientsEval'),
    url(r'^patientEval/$', 'patientEvalView', name='patientEval'),
)
