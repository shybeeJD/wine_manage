from django.db import models

# Create your models here.

class Address(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    label=models.CharField(max_length=32)
    address=models.CharField(max_length=64)
    detial=models.CharField(max_length=64)
    delete=models.IntegerField()
