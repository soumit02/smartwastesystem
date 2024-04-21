from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bin(models.Model):
    Bin_id = models.CharField(max_length=100)
    Bin_location = models.CharField(max_length=100)
    Bin_capacity = models.FloatField()

    def __str__(self):
        return self.Bin_id
