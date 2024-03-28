from django import forms
from django.forms import ModelForm
from .models import Criteria,Alternative

class CriteriaForm(ModelForm):
    class Meta:
        model = Criteria
        fields = '__all__'

        labels = {
            'code':"Criteria Id",
            'name':"Criteria Name",
            'attribute':"Attribute",
            'weight':"Weight"
        }
        const_fields = {'class': 'form-control','style':"width:400px"}

        widgets = {
            'code':forms.TextInput(attrs=const_fields),
            'name':forms.TextInput(attrs=const_fields),
            'weight':forms.NumberInput(attrs=const_fields),
        }

class AlternativeForm(ModelForm):
    class Meta:
        model = Alternative
        fields = '__all__'
        const_fields = {'class': 'form-control','style':"width:400px"}
        
        widgets = {
            'value':forms.NumberInput(attrs=const_fields),
            'criteria':forms.Select(attrs=const_fields),
            'student':forms.Select(attrs=const_fields)
        }
    
    # make it query to asc in select components
    def __init__(self, *args, **kwargs):
        super(AlternativeForm, self).__init__(*args, **kwargs)
        self.fields['criteria'].queryset = Criteria.objects.order_by('id')