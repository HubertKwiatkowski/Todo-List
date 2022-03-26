from django import forms
from django.conf import settings
from django.template.loader import render_to_string

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'

class ColorWidget(forms.TextInput):

    template_name = "colorfield/color.html"

    class Media:
        if settings.DEBUG:
            js = [
                "colorfield/jscolor/jscolor.js",
                "colorfield/colorfield.js",
            ]
        else:
            js = [
                "colorfield/jscolor/jscolor.min.js",
                "colorfield/colorfield.js",
            ]

    def get_context(self, name, value, attrs=None):
        context = {}
        context.update(self.attrs.copy() or {})
        context.update(attrs or {})
        context.update(
            {
                "widget": self,
                "name": name,
                "value": value,
            }
        )
        return context

    def render(self, name, value, attrs=None, renderer=None):
        return render_to_string(
            self.template_name, self.get_context(name, value, attrs)
        )