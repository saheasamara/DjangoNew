from django.db import models


# Create your models here.

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=120)
    order_tel = models.CharField(max_length=20)
