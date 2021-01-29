from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Submit,
)
from .models import Project

class ProjectForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'form-label mt-3'
        self.helper.layout = Layout(
            Field('client', css_class='form-select'),
            Field('name', placeholder='Username'),
            Field('description', placeholder='Contact'),
            Field('start_date'),
            Field('end_date'),
            Field('worker', css_class='form-select'),
            Field('status', css_class='form-select'),
    )
        
    class Meta:
        model = Project
        exclude = ['created_at', 'uuid']
        # widgets = {
        #     'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select start date', 'type':'date', 'min':'2018-01-01', 'max':'2030-12-31'}),
        #     'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select end date', 'type':'date', 'min':'2018-01-01', 'max':'2030-12-31'}),
        # }
        widgets = {
            'start_date' : forms.TextInput(attrs={'type': 'date', 'min':'2018-01-01', 'max':'2030-12-31'}),
            'end_date' : forms.TextInput(attrs={'type': 'date', 'min':'2018-01-01', 'max':'2030-12-31'}),
        }