# Create your models here.
from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=50)
    property_type = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
