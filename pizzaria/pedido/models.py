from django.db import models
from pizza.models import Pizza

from django.core.exceptions import ValidationError

# Create your models here.
class PedidoStatusChoices(models.TextChoices):
    AGUARDANDO_CONFIRMACAO = 'AGUARDANDO_CONFIRMACAO', 'Aguardando Confirmação'
    CONFIRMADO = 'CONFIRMADO'
    FINALIZADO = 'FINALIZADO'
    SAIU_PARA_ENTREGA = 'SAIU_PARA_ENTREGA'
    ENTREGUE = 'ENTREGUE'


class Pedido(models.Model):
    cliente = models.CharField(editable=True, max_length=60)
    data_do_pedido = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    status = models.CharField(max_length=60, choices=PedidoStatusChoices.choices, default=PedidoStatusChoices.AGUARDANDO_CONFIRMACAO)

    def __str__(self):
        return self.cliente


class Endereco(models.Model):
    bairro = models.CharField(editable=True, max_length=60, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Endereço"


class Item(models.Model):
    quantidade = models.IntegerField(editable=True, default=1)

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT)

    def save(self, *args, **kwars):
        super().save(*args, **kwars)

#    def save(self, *args, **kwargs):
#         if not self.id:
#             self.id = timezone.now(default=now)