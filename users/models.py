from django.db import models
#creation of the user model #3
# Create your models here.
PROFILE_CHOICES = (
    ('client', 'Cliente'),
    ('professional', 'Profissional')
)

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    profile = models.CharField(max_length=15, choices=PROFILE_CHOICES, default='client')
    
class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_phone_numbers')
    number = models.CharField(max_length=15)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_addresses')
    street = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=100)
    house_number = models.CharField(max_length=5)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=20)