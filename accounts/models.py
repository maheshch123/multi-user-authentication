from django.db import models

from datetime import date


# Create your models here.

class marks(models.Model):
    name = models.CharField(max_length=100)
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    sub4 = models.IntegerField()
    sub5 = models.IntegerField()
    Dob = models.DateField(blank=True,null=True)
