from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from . import models

class UserForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username', 'name', 'email', 'profile']

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

class CustomAuthenticationForm(AuthenticationForm):
    pass 