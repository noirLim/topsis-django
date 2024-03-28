from django import forms
from django.forms import ModelForm
from .models import Result

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = '__all__'

        const_fields = {'class':'form-control','style':"width:400px"}

        widgets = {
            'name':forms.TextInput(attrs=const_fields),
            'email':forms.EmailInput(attrs=const_fields),
            'date':forms.DateInput(attrs={'type': 'date','class':'form-control'})
        }
