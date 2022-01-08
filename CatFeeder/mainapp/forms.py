from django import forms
from django.db import models
from django.forms import DateTimeInput, DateTimeField

from .models import Meals, Medication


class MealsEntryForm(forms.ModelForm):

    class Meta:
        model = Meals
        fields = ['size']


class ManualTimeEntryForm(forms.ModelForm):
    entryTime = DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"], required=False)

    class Meta:
        model = Meals
        fields = ['size', 'entryTime']


class ManualMedTime(forms.ModelForm):
    entryTime = DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"], required=False)

    class Meta:
        model = Medication
        fields = ['entryTime']



