from django.contrib import admin
from .models import PatientEval, Document

admin.site.register(PatientEval)
admin.site.register(Document)

#class ChoiceInline(admin.StackedInline):
#    model = EvalChoice
#    extra = 3

#class EvalAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['question']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
#    inlines = [ChoiceInline]

#admin.site.register(PatientEval, EvalAdmin)

#import models
#from django.contrib import admin

#admin.site.register(models.Question)
#admin.site.register(models.Choice)