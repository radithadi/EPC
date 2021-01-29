from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Submit,
)
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from .models import Timesheet

class TimesheetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'form-label mt-3'
        self.helper.layout = Layout(
            Field('project', css_class='form-select'),
            Field('date'),
            Field('activity', css_class='form-select'),
            Field('description', placeholder='Contact'),
            Field('location', placeholder='Location'),
    )
        
    class Meta:
        model = Timesheet
        exclude = ['user', 'uuid']
        widgets = {
            'user' : forms.TextInput(attrs={'type': 'hidden'}),
            'date' : forms.TextInput(attrs={'type': 'date', 'min':'2018-01-01', 'max':'2030-12-31'}),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }