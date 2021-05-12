from django.db import models

# Create your models here.

class Pizza(models.Model):
    sabor = models.CharField(unique=True, editable=True, max_length=60)
    preco = models.FloatField("preço", editable=True)

    ativo = models.BooleanField(default=True)

    ingredientes = models.TextField(null=True)

    def __str__(self):
        if self.ativo == True:
            ativo = 'Estamos Fazendo!'

        else:
            ativo = 'Desculpe, não estamos fazendo'

        return f'{self.sabor} - {self.preco} - {ativo}'