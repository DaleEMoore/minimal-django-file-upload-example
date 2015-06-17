# -*- coding: utf-8 -*-
from django import forms
from .models import PatientEval

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class PatientsEvalForm(forms.Form):
    patientsEval = forms.ModelChoiceField(
        queryset=PatientEval.objects.all(),
        label='Select a patient'
    )

class PatientEvalForm(forms.Form):
    patientEval = forms.ModelChoiceField(
        queryset=PatientEval.objects.first(),
        label='Select a patient'
    )