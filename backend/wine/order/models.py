from django.db import models

# Create your models here.

class Order(models.Model):
    id=models.AutoField(primary_key=True)
    userId=models.IntegerField()
    status=models.IntegerField()
    goods=models.CharField(max_length=256)
    packingPrice=models.FloatField()
    deliveryPrice=models.FloatField()
    discount=models.FloatField()
    address=models.IntegerField()
    deliveryMan=models.IntegerField()
    paymentChannels=models.IntegerField()
    addTime=models.DateTimeField(auto_now=True)


