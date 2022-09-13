from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=35)
    birth = models.DateField(null=False)
    color = models.CharField(max_length=20)