from django.db import models
from django.contrib.auth.models import AbstractUser

PROFILE_CHOICES = (
    ('client', 'Cliente'),
    ('professional', 'Profissional')
)

class CustomUser(AbstractUser):  # Herdando de AbstractUser
    email = models.EmailField(unique=True)  #forçamos a unicidade
    profile = models.CharField(max_length=15, choices=PROFILE_CHOICES, default='client')

    def __str__(self):
        return self.username  # Melhor usar username como identificador

class PhoneNumber(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='phone_numbers')
    number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.number}"

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=100)
    house_number = models.CharField(max_length=5)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.street}, {self.city}, {self.house_number}"
