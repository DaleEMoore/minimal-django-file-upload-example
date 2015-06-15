# -*- coding: utf-8 -*-
from django import forms
from .models import PatientEval

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class PatientEvalForm(forms.Form):
    patientEval = forms.ModelChoiceField(
        queryset=PatientEval.objects.all(),
        label='Select a patient'
    )