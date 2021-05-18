from django.contrib import admin
from django import forms
from pedido.models import Pedido, Item
from pizza.models import Pizza

# Register your models here.
class ItemTabularAdmin(admin.TabularInline):
    list_display = ['quantidade', 'pizza']
    extra = 1
    model = Item


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_do_pedido', 'confirmado','cancelado', 'finalizado', 'saiu_para_entrega', 'entregue']
    readonly_fields = ['data_do_pedido']
    list_filter = ['data_do_pedido', 'confirmado', 'cancelado', 'finalizado', 'saiu_para_entrega', 'entregue']

    ordering = ['-data_do_pedido']

    inlines = [ItemTabularAdmin]

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['bairro']

admin.site.register(Pedido, PedidoAdmin)