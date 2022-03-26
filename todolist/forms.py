from django import forms
# from django.forms import ModelForm
from .widget import *


class TagForm(forms.ModelForm):
    tagName = forms.CharField(max_length=50, label='Tag')
    tagColor = forms.CharField(max_length=7, label='Color', required=False, widget=ColorWidget)


class ItemForm(forms.Form):
    taskName = forms.CharField(max_length=200)
    taskDone = forms.BooleanField(required=False)
    taskNote = forms.CharField(required=False, widget=forms.Textarea)
    taskStartDate = forms.DateField(
        required=False, 
        widget=DatePickerInput
    )    
    taskStartTime = forms.TimeField(
        required=False, 
        widget=TimePickerInput
    )
    taskEndDate = forms.DateField(
        required=False, 
        widget=DatePickerInput
    )    
    taskEndTime = forms.TimeField(
        required=False, 
        widget=TimePickerInput
    )
    # taskTags = forms.CharField(required=False)