from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Submit,
)
from .models import Company

class CompanyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        self.helper.label_class = 'form-label mt-3'
        self.helper.layout = Layout(
            Field('name', placeholder='Username'),
            Field('address', placeholder='Adress'),
            Field('city', placeholder='City'),
            #Submit('submit', 'Submit', css_class='float-right')  # define your signup button here
    )
        
    class Meta:
        model = Company
        exclude = ['code']