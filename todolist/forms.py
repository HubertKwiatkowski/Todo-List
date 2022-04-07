from time import timezone
from django import forms
from django.utils import timezone as dtz
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


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

    task_start_date = forms.DateField(
        required=False, 
        widget=DatePickerInput,
    )    
    task_start_time = forms.TimeField(
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