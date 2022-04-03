from time import timezone
from django import forms
from django.utils import timezone as dtz
from .models import *


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


# class TagForm(forms.ModelForm):
#     tagName = forms.CharField(max_length=50, label='Tag')
#     tagColor = forms.CharField(max_length=7, label='Color', required=False, widget=ColorWidget)


class ItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = '__all__'

    task_start_date = forms.DateTimeField(
        required=False, 
        widget=DatePickerInput,
    )    
    task_start_time = forms.DateTimeField(
        required=False, 
        widget=TimePickerInput
    )
    task_end_date = forms.DateField(
        required=False, 
        widget=DatePickerInput,
    )    
    task_end_time = forms.TimeField(
        required=False, 
        widget=TimePickerInput
    )
    # taskName = forms.CharField(max_length=200)
    # taskDone = forms.BooleanField(required=False)
    # taskNote = forms.CharField(required=False, widget=forms.Textarea)
    # taskStartDate = forms.DateField(
    #     required=False, 
    #     widget=DatePickerInput
    # )    
    # taskStartTime = forms.TimeField(
    #     required=False, 
    #     widget=TimePickerInput
    # )
    # taskEndDate = forms.DateField(
    #     required=False, 
    #     widget=DatePickerInput
    # )    
    # taskEndTime = forms.TimeField(
    #     required=False, 
    #     widget=TimePickerInput
    # )
    # taskTags = forms.CharField(required=False)