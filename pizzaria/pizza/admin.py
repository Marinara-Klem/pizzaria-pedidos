from django.contrib import admin
from pizza.models import Pizza

# Register your models here.


class PizzaAdmin(admin.ModelAdmin):
    list_display = ['sabor', 'preco', 'ativo']
    list_filter = ['ativo']

admin.site.register(Pizza, PizzaAdmin)