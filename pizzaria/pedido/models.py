from django.db import models
from pizza.models import Pizza

from django.core.exceptions import ValidationError

# Create your models here.


class Pedido(models.Model):
    cliente = models.CharField(editable=True, max_length=60)

    data_do_pedido = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return self.cliente


class Item(models.Model):
    quantidade = models.IntegerField(editable=True, default=1)
    
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT)

    def clean(self):
        if not self.pizza.ativo:
            raise ValidationError({'pizza': 'Não estamos fazendo este sabor hoje'})

    is_cleaned = True

    def save(self, *args, **kwars):
        if not self.is_cleaned:
            self.clean()
        self.is_cleaned = False

        super().save(*args, **kwars)

#    def save(self, *args, **kwargs):
#         if not self.id:
#             self.id = timezone.now(default=now)