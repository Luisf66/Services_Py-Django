from django import forms
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = models.PhoneNumber
        fields = ['number']  # Campos do PhoneNumber

class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = [
            'street',
            'neighborhood',
            'house_number',
            'city',
            'state',
            'zip_code'
        ]  # Campos do Address
