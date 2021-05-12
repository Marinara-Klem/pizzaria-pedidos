from django.db import models
from pizza.models import Pizza

# Create your models here.


class Pedido(models.Model):
    cliente = models.CharField(editable=True, max_length=60)


class Item(models.Model):
    quantidade = models.IntegerField(editable=True, default=1)
    
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT)
