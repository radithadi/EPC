from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Submit,
)
from .models import Advance

class AdvanceForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'form-label mt-3'
        self.helper.layout = Layout(
            Field('project', css_class='form-select'),
            Field('name', placeholder='Name'),
            Field('category', css_class='form-select'),
            Field('description', placeholder='Contact'),
            Field('date'),
            Field('ammount', placeholder='Ammount'),
            Field('status', css_class='form-select'),
    )
        
    class Meta:
        model = Advance
        exclude = ['user','uuid']
        widgets = {
            'date' : forms.TextInput(attrs={'type': 'date', 'min':'2018-01-01', 'max':'2030-12-31'}),
        }