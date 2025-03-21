from django import forms
from .models import Service
import re

class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Não é possível cadastrar um serviço com preço negativo.')
        return price
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match('^[a-zA-Z0-9\s]+$', name):
            raise forms.ValidationError('O nome do serviço deve conter apenas letras, números e espaços.')
        return name