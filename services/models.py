from django.db import models

# Create your models here.
class Service(models.Model):
    #STATUS_CHOICES = [
        #('pending', 'Pendente'),
        #('accepted', 'Aceito'),
        #('completed', 'Concluído'),
        #('canceled', 'Cancelado'),
    #]

    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    photo = models.ImageField(upload_to='services/', null=True, blank=True)
    #requester = models.ForeignKey(User, on_delete=models.PROTECT)
    #provider = models.ForeignKey(User, on_delete=models.PROTECT)
    #date = models.DateField(auto_now_add=True)
    #hours = models.TimeField(auto_now_add=True)
    #rating = models.FloatField(null=True, blank=True)
    #status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.name}'