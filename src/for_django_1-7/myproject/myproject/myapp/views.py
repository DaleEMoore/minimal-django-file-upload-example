# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document
from .forms import DocumentForm
from .models import PatientEval
from .forms import PatientEvalForm
#from .models import PatientEvals
from .forms import PatientsEvalForm

def documentsView(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.documents'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/documents.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def patientsEvalView(request):
    # Handle file upload
    if request.method == 'POST':
        form = PatientsEvalForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = PatientEval(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.patientsEval'))
    else:
        form = PatientsEvalForm() # A empty, unbound form

    # Load documents for the list page
    patientsEval = PatientEval.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/patientsEval.html',
        {'patientsEval': patientsEval, 'form': form},
        context_instance=RequestContext(request)
    )

def patientEvalView(request):
    # Handle file upload
    if request.method == 'POST':
        form = PatientEvalForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = PatientEval(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.patientEval'))
    else:
        form = PatientEvalForm() # A empty, unbound form

    # Load documents for the list page
    patientEval = PatientEval.objects.first()
    #patientEvals = PatientEval.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/patientEval.html',
        {'patientEval': patientEval, 'form': form},
        context_instance=RequestContext(request)
    )
