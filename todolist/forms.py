from django import forms
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput


class TagForm(forms.Form):
    tagName = forms.CharField(max_length=50, label='Tag')
    tagColor = forms.CharField(max_length=7, label='Color', required=False)


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