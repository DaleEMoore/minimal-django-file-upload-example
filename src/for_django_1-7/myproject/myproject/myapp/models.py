# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime

class PatientEval(models.Model):
    primary_care_doctor_name = models.CharField(max_length=200)
    marketers_initials_name = models.CharField(max_length=200, null=True, blank=True)
    patient_eval_date = models.DateField()
    patient_injury_date = models.DateField()
    patient_name = models.CharField(max_length=200)
    diagnosis_surgery = models.CharField(max_length=200)
    """
    Service (multiple selection)
        Evaluate and Treat
        Physical Medicine Consultation/Therapy
        Neurology Consultation
        Pain Management
        """
    evaluate_and_treat = models.NullBooleanField(default=False)
    physical_medicine_consultation_therapy = models.NullBooleanField(default=False)
    neurology_consultation = models.NullBooleanField(default=False)
    pain_management = models.NullBooleanField(default=False)
    """
    Physicians (multiple selection)
        Robert Lowry, MD, MS (Surgery, PMR - Musculoskelital)
        Dennis Barson, DO (Neurology)
        Dean Parsons, DC
        """
    robert_lowry = models.NullBooleanField(default=False)
    dennis_barson = models.NullBooleanField(default=False)
    dean_parsons = models.NullBooleanField(default=False)
    """
    Neurology Division (multiple selection)
        NCV/EMG
        UE''s
        LE''s
        EEG
        Ambulatory EEG
        """
    ncv_emg = models.NullBooleanField(default=False)
    les = models.NullBooleanField(default=False)
    ues = models.NullBooleanField(default=False)
    eeg = models.NullBooleanField(default=False)
    nd_ambulatory_eeg = models.NullBooleanField(default=False)
    """
    Physical Medicine & Rehabilitation Division/Therapy (?)
        Acute Injury
        Postoperative Care
        Chronic Pain
        Ambulatory EEG
        """
    acute_injury = models.CharField(max_length=200, null=True, blank=True)
    chronic_pain = models.CharField(max_length=200, null=True, blank=True)
    post_operative_care = models.CharField(max_length=200, null=True, blank=True)
    pm_ambulatory_eeg = models.CharField(max_length=200, null=True, blank=True)
    """
    Frequency (just 1 selection)
        2 x / wk - 4 wks
        3 x / wk - 4 wks
        2 x / wk - 6 wks
        3 x / wk - 6 wks
        3 x / wk - 1 wk
        A x / wk - B wks
        """
    freq_per_week = models.IntegerField(null=True, blank=True)
    freq_weeks = models.IntegerField(null=True, blank=True)
    """
    Return to Work (multiple selection)
        Pre-Employment Exams
        FCE''s
        Fit For Duty/Drug Screenings
        Impairment Ratings
        DOT Exams
        Work Conditioning
        """
    pre_employment_exams = models.NullBooleanField(default=False)
    fce_s = models.NullBooleanField(default=False)
    fit_for_duty_drug_screenings= models.NullBooleanField(default=False)
    impairment_ratings = models.NullBooleanField(default=False)
    dot_exams = models.NullBooleanField(default=False)
    work_conditioning = models.NullBooleanField(default=False)
    #return_to_work_choices = (
    #    ('Pre-Employment Exams', 'Pre-Employment Exams'),
    #    ("FCE's", "FCE's"),
    #    ('Fit For Duty/Drug Screenings', 'Fit For Duty/Drug Screenings'),
    #    ('Impairment Ratings', 'Impairment Ratings'),
    #    ('DOT Exams', 'DOT Exams'),
    #    ('Work Conditioning', 'Work Conditioning'),
    #
    #return_to_work = models.CharField(max_length=30, choices=return_to_work_choices, null=True, blank=True)
    """
    Goals (multiple selection)
        Improve ADL''s
        Reduce Pain
        Reduce Swelling/Edema
        Restore Joint ROM
        Scar Management
        Normal Sensation/Desensitize
        Increase Strength
        Decrease Strength
        Other: _____________________
    """
    improve_adls = models.NullBooleanField(default=False)
    reduce_pain = models.NullBooleanField(default=False)
    reduce_swelling_edema = models.NullBooleanField(default=False)
    restore_joint_rom = models.NullBooleanField(default=False)
    scar_management = models.NullBooleanField(default=False)
    normal_sensation_desensitize = models.NullBooleanField(default=False)
    increase_strength = models.NullBooleanField(default=False)
    decrease_strength = models.NullBooleanField(default=False)
    goals_other = models.CharField(max_length=30)

    referring_doctor = models.CharField(max_length=30)
    logged_in_user = models.CharField(max_length=30)
    #uploaded_files = models.ForeignKey(Document)
    #uploaded_files = models.FileField(default='', upload_to='documents/%Y/%m/%d')
    #question = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.patient_name


class Document(models.Model):
    #patientEval = models.ForeignKey(PatientEval, default='')
    docfile = models.FileField(default='',upload_to='documents/%Y/%m/%d')
    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s' % (self.docfile)
        #return u'%s: %s' % (self.patientEval, self.docfile)

#class Document(models.Model):
#    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
#   def __unicode__(self):  # Python 3: def __str__(self):
#        return self.patient_name

