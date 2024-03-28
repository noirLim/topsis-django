from django import forms
from django.forms import ModelForm
from .models import Students

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        labels = {
            'code':"Student Id",
            'name':"Student Name"
        }

        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control','style':"width:400px",}),
            'name': forms.TextInput(attrs={'class': 'form-control','style':"width:400px",}),
        }