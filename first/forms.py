from django import forms
from django.db.models import fields
from .import models

class Studentform(forms.ModelForm):
    class Meta:
        model = models.Student
        fields= "__all__"
