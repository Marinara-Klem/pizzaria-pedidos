from django.db import models

# Create your models here.

class Pizza(models.Model):
    sabor = models.CharField(unique=True, editable=True, max_length=60)
    preco = models.FloatField("preço", editable=True)

    def __str__(self):
        return self.sabor