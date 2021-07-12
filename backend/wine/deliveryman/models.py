from django.db import models

# Create your models here.
class Deliveryman(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    phone=models.CharField(max_length=18)
    registerTime=models.DateTimeField(auto_now=True)

