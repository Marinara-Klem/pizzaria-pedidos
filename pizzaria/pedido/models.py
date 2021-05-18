from django.db import models
from pizza.models import Pizza

from django.core.exceptions import ValidationError

# Create your models here.

class Endereco(models.Model):
    bairro = models.CharField(editable=True, max_length=60, null=True)

    class Meta:
        verbose_name = "Endereço"

class Pedido(models.Model):
    cliente = models.CharField(editable=True, max_length=60)

    data_do_pedido = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    confirmado = models.BooleanField(default=False)
    cancelado = models.BooleanField(default=False)
    finalizado = models.BooleanField(default=False)
    saiu_para_entrega = models.BooleanField(default=False)
    entregue = models.BooleanField(default=False)

    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.cliente

class Item(models.Model):
    quantidade = models.IntegerField(editable=True, default=1)
    
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT)

    is_cleaned = True

    def save(self, *args, **kwars):
        if not self.is_cleaned:
            self.clean()
        self.is_cleaned = False

        super().save(*args, **kwars)

#    def save(self, *args, **kwargs):
#         if not self.id:
#             self.id = timezone.now(default=now)