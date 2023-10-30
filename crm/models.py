from django.db import models


# Create your models here.

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=120, verbose_name='Имя')
    order_tel = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказ'


class MyClass(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=120)
