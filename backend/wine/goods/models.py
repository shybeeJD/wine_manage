from django.db import models

# Create your models here.
class Goods(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    price=models.IntegerField()
    stock=models.IntegerField()
    category=models.CharField(max_length=32)
    alcohol=models.CharField(max_length=8)
    capacity=models.CharField(max_length=10)
    brand=models.CharField(max_length=32)
    shelfLife=models.CharField(max_length=10)
    pic=models.CharField(max_length=256)
    belong=models.IntegerField()
    delete=models.IntegerField()
    addTime=models.DateTimeField(auto_now=True)


