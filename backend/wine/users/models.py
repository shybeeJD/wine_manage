from django.db import models

# Create your models here.


class Users(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=67)
    phone=models.CharField(max_length=20)
    register_time=models.DateTimeField(auto_now=True)
