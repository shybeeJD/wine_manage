from django.db import models

# Create your models here.

class Warehouse(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=15)
    lat=models.FloatField()
    lng=models.FloatField()
    addTime=models.DateTimeField(auto_now=True)


